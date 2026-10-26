# -*- coding: utf-8 -*-
"""
Bien soan DE CUONG ON TAP GIUA KI I - TIN HOC 10 (dinh huong ICT,
bo sach Ket noi tri thuc) thanh file PDF.

Nguon: "MA TRAN GIUA KI I - LOP 10.docx" (ma tran de + dac ta de kiem tra).
Toan bo van ban goc duoc nho vao SOURCE_DATA (trich xuat tu word/document.xml)
va duoc tai hien nguyen ven o Phu luc A.

Chay: python3 tools/build_de_cuong.py
Can: reportlab (pip install reportlab), font DejaVu (co san tren he thong).
"""
import base64
import html
import json
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

# --------------------------------------------------------------------------
# 1. Du lieu goc (nguyen van, trich tu file .docx)
# --------------------------------------------------------------------------
SOURCE_DATA = json.loads(base64.b64decode(
    "WwogewogICJ0eXBlIjogInAiLAogICJ0ZXh0IjogIk1BIFRS4bqsTiDEkOG7gCBLSeG7gk0gVFJBIEdJ4buuQSBLw4wgSSAiCiB9LAogewogICJ0eXBlIjogInAiLAogICJ0ZXh0IjogIk3DlE46IFRJTiBI4buMQyAxMCAtIMSQ4buKTkggSMav4buaTkcgSUNUICIKIH0sCiB7CiAgInR5cGUiOiAiYm9va21hcmtFbmQiCiB9LAogewogICJ0eXBlIjogInAiLAogICJ0ZXh0IjogIi0gVGjhu51pIGdpYW4gbMOgbSBiw6BpOiA0NSBwaMO6dC4iCiB9LAogewogICJ0eXBlIjogInAiLAogICJ0ZXh0IjogIi0gSMOsbmggdGjhu6ljIGtp4buDbSB0cmE6IEvhur90IGjhu6NwIGdp4buvYSB0cuG6r2MgbmdoaeG7h20gdsOgIHThu7EgbHXhuq1uICh04buJIGzhu4cgNzAlIHRy4bqvYyBuZ2hp4buHbSwgMzAlIHThu7EgbHXhuq1uKS4iCiB9LAogewogICJ0eXBlIjogInAiLAogICJ0ZXh0IjogIi0gQ+G6pXUgdHLDumM6IgogfSwKIHsKICAidHlwZSI6ICJwIiwKICAidGV4dCI6ICIrIE3hu6ljIMSR4buZIMSR4buBOiA3MCUgdHLhuq9jIG5naGnhu4dtICg0MCAlIE5o4bqtbiBiaeG6v3Q7IDIwICUgVGjDtG5nIGhp4buDdTsgMTAlIFbhuq1uIGThu6VuZyksIDMwJSB04buxIGx14bqtbiAoMTAlIFRow7RuZyBiaeG7g3UsIDEwJSBW4bqtbiBk4bulbmc7IDEwJSBW4bqtbiBk4bulbmcgY2FvKS4iCiB9LAogewogICJ0eXBlIjogInAiLAogICJ0ZXh0IjogIisgUGjhuqduIHRy4bqvYyBuZ2hp4buHbTogNywwIMSRaeG7g20gKGfhu5NtIDIwIGPDonUgaOG7j2kgdHLhuq9jIG5naGnhu4dtIDQgbOG7sWEgY2jhu41uLCBt4buXaSBjw6J1IDAsMjUgxJFp4buDbTsgMiBjw6J1IGzhu7FhIGNo4buNbiDEkcO6bmcvc2FpLCBt4buXaSBjw6J1IDEsMCDEkWnhu4NtKSIKIH0sCiB7CiAgInR5cGUiOiAicCIsCiAgInRleHQiOiAiKyBQaOG6p24gdOG7sSBsdeG6rW46IDMsMCDEkWnhu4NtICgxIGPDonUgdGjDtG5nIGhp4buDdTogMSwwIMSRaeG7g207IDEgY8OidSB24bqtbiBk4bulbmc6IDEsMCDEkWnhu4NtOyAxIGPDonUgduG6rW4gZOG7pW5nIGNhbzogMSwwIMSRaeG7g20pLiIKIH0sCiB7CiAgInR5cGUiOiAidGJsIiwKICAicm93cyI6IFsKICAgWwogICAgewogICAgICJ0ZXh0IjogIlRUIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6ICJyZXN0YXJ0IgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJO4buZaSBkdW5nIGtp4bq/biB0aOG7qWMva8SpIG7Eg25nIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6ICJyZXN0YXJ0IgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICLEkMahbiB24buLIGtp4bq/biB0aOG7qWMva8SpIG7Eg25nIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6ICJyZXN0YXJ0IgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJN4bupYyDEkeG7mSBuaOG6rW4gdGjhu6ljIiwKICAgICAic3BhbiI6IDE0LAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIlThu5VuZyUgxJFp4buDbSIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAicmVzdGFydCIKICAgIH0KICAgXSwKICAgWwogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIk5o4bqtbiBiaeG6v3QiLAogICAgICJzcGFuIjogNCwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJUaMO0bmcgaGnhu4N1IiwKICAgICAic3BhbiI6IDQsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiVuG6rW4gZOG7pW5nIiwKICAgICAic3BhbiI6IDMsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiVuG6rW4gZOG7pW5nIGNhbyIsCiAgICAgInNwYW4iOiAzLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9CiAgIF0sCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogImNvbnRpbnVlIgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogImNvbnRpbnVlIgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogImNvbnRpbnVlIgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJUTiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIsSQUyIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIlRMIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiVE4iLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICLEkFMiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJUTCIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIlROIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAixJBTIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiVEwiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJUTiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIsSQUyIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIlRMIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0KICAgXSwKICAgWwogICAgewogICAgICJ0ZXh0IjogIjEiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogInJlc3RhcnQiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIkNo4bunIMSR4buBIEEuIE3DoXkgdMOtbmggdsOgIHjDoyBo4buZaSB0cmkgdGjhu6ljIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6ICJyZXN0YXJ0IgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIxLiBE4buvIGxp4buHdSwgdGjDtG5nIHRpbiB2w6AgeOG7rSBsw70gdGjDtG5nIHRpbi4iLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjEiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyMCVcbigyIMSRaeG7g20pIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0KICAgXSwKICAgWwogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjIuIFZhaSB0csOyIGPhu6dhIG3DoXkgdMOtbmggdsOgIGPDoWMgdGhp4bq/dCBi4buLIHRow7RuZyBtaW5oIHRyb25nIG7hu4FuIGtpbmggdOG6vyB0cmkgdGjhu6ljIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiNCIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjIgw70iLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyIMO9IiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiXG4iLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyMCVcbigyIMSRaeG7g20pIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0KICAgXSwKICAgWwogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjMuIEvEqSBuxINuZyBz4butIGThu6VuZyB0aGnhur90IGLhu4sgc+G7kSBj4bunYSBt4buXaSBjw7RuZyBkw6JuLiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9CiAgIF0sCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICIyIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6ICJyZXN0YXJ0IgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJDaOG7pyDEkeG7gSBCLiBN4bqhbmcgbcOheSB0w61uaCB2w6AgSW50ZXJuZXQiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogInJlc3RhcnQiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjEuIEtow6FpIG5p4buHbSBt4bqhbmcgbcOheSB0w61uaCwgSW50ZXJuZXQsIElvVC4gUGjDom4gbG/huqFpIG3huqFuZyBtw6F5IHTDrW5oIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiNCIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjIgw70iLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyIMO9IiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiXG4iLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyMCVcbigyIMSRaeG7g20pIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0KICAgXSwKICAgWwogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjIuIFPhu60gZOG7pW5nIGThu4tjaCB24bulIHdlYi4gVOG7sSBi4bqjbyB24buHIGtoaSB0aGFtIGdpYSBt4bqhbmciLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICI0IiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMSIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjIwICVcbigyIMSRaeG7g20pIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0KICAgXSwKICAgWwogICAgewogICAgICJ0ZXh0IjogIjMiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJDaOG7pyDEkeG7gSBELiDEkOG6oW8gxJHhu6ljLCBwaMOhcCBsdeG6rXQgdsOgIHbEg24gaG/DoSB0cm9uZyBtw7RpIHRyxrDhu51uZyBz4buRIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMS4gTmdoxKlhIHbhu6UgdHXDom4gdGjhu6cgcGjDoXAgbMOtIHRyb25nIG3DtGkgdHLGsOG7nW5nIHPhu5EiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjEiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyMCAlXG4oMiDEkWnhu4NtKSIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9CiAgIF0sCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICJU4buVbmciLAogICAgICJzcGFuIjogMywKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIxNiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjQiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICI0IMO9IiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMSIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjQgw70iLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIxIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMSIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9CiAgIF0sCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICJU4buJIGzhu4cgJSB04burbmcgbeG7qWMgxJHhu5kgbmjhuq1uIHRo4bupYyIsCiAgICAgInNwYW4iOiAzLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjQwIiwKICAgICAic3BhbiI6IDQsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMzAiLAogICAgICJzcGFuIjogMywKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyMCIsCiAgICAgInNwYW4iOiA0LAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjEwIiwKICAgICAic3BhbiI6IDMsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMTAiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfQogICBdLAogICBbCiAgICB7CiAgICAgInRleHQiOiAiVOG7iSBs4buHIGNodW5nIiwKICAgICAic3BhbiI6IDMsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiNzAiLAogICAgICJzcGFuIjogNywKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIzMCIsCiAgICAgInNwYW4iOiA3LAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjEwMCIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9CiAgIF0KICBdCiB9LAogewogICJ0eXBlIjogInAiLAogICJ0ZXh0IjogIiIKIH0sCiB7CiAgInR5cGUiOiAicCIsCiAgInRleHQiOiAixJDhurdjIHThuqMgxJHhu4Ega2nhu4NtIHRyYSBnaeG7r2Ega8OsIEkiCiB9LAogewogICJ0eXBlIjogInRibCIsCiAgInJvd3MiOiBbCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICJUVCIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAicmVzdGFydCIKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiTuG7mWkgZHVuZyBraeG6v24gdGjhu6ljL2vEqSBuxINuZyIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAicmVzdGFydCIKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAixJDGoW4gduG7iyBraeG6v24gdGjhu6ljL2vEqSBuxINuZyIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAicmVzdGFydCIKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiTeG7qWMgxJHhu5kga2nhur9uIHRo4bupYywga8SpIG7Eg25nXG5j4bqnbiBraeG7g20gdHJhLCDEkcOhbmggZ2nDoSIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAicmVzdGFydCIKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiU+G7kSBjw6J1IGjhu49pIHRoZW8gY8OhYyBt4bupYyDEkeG7mSBuaOG6rW4gdGjhu6ljIiwKICAgICAic3BhbiI6IDgsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0KICAgXSwKICAgWwogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIk5o4bqtbiBiaeG6v3QiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJUaMO0bmcgaGnhu4N1IiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiVuG6rW4gZOG7pW5nIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiVuG6rW4gZOG7pW5nIGNhbyIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9CiAgIF0sCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICIxIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6ICJyZXN0YXJ0IgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJDaOG7pyDEkeG7gSBBLiBNw6F5IHTDrW5oIHbDoCB4w6MgaOG7mWkgdHJpIHRo4bupYyIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAicmVzdGFydCIKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMS4gROG7ryBsaeG7h3UsIHRow7RuZyB0aW4gdsOgIHjhu60gbMO9IHRow7RuZyB0aW4iLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJOaOG6rW4gYmnhur90XG5cdOKAkyBOw6p1IMSRxrDhu6NjIHPhu7EgxrB1IHZp4buHdCBj4bunYSB2aeG7h2MgbMawdSB0cuG7ryBk4buxYSB0csOqbiBjw6FjIHRoaeG6v3QgYuG7iyBz4buRLlxuVGjDtG5nIGhp4buDdVxu4oCTIFBow6JuIGJp4buHdCDEkcaw4bujYyB0aMO0bmcgdGluIHbDoCBk4buvIGxp4buHdSxcbuKAkyBOw6p1IMSRxrDhu6NjIHbDrSBk4bulIG1pbmggaG/huqEgduG7gSB0aMO0bmcgdGluIHbDoCBk4buvIGxp4buHdS5cblbhuq1uIGThu6VuZ1xu4oCTIENodXnhu4NuIMSR4buVaSDEkcaw4bujYyBnaeG7r2EgY8OhYyDEkcahbiB24buLIGzGsHUgdHLhu68gdGjDtG5nIHRpbjogQiwgS0IsIE1CLC4uLlxuXHTigJMgWOG7rSBsw60gdsOgIHRydXnhu4FuIHRow7RuZyB0aW4gYuG6sW5nIHRoaeG6v3QgYuG7iyBz4buRLiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjIgKFROKSIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjIgKFROKSIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjEgKFRMKSIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9CiAgIF0sCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogImNvbnRpbnVlIgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogImNvbnRpbnVlIgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIyLiBWYWkgdHLDsiBj4bunYSBtw6F5IHTDrW5oIHbDoCBjw6FjIHRoaeG6v3QgYuG7iyB0aMO0bmcgbWluaCB0cm9uZyBu4buBbiBraW5oIHThur8gdHJpIHRo4bupYyIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIk5o4bqtbiBiaeG6v3RcbuKAkyBUcsOsbmggYsOgeSDEkcaw4bujYyBuaOG7r25nIMSRw7NuZyBnw7NwIGPGoSBi4bqjbiBj4bunYSB0aW4gaOG7jWMgxJHhu5FpIHbhu5tpIHjDoyBo4buZaS5cbuKAkyBOaOG6rW4gYmnhur90IMSRxrDhu6NjIG3hu5l0IHbDoGkgdGhp4bq/dCBi4buLIHPhu5EgdGjDtG5nIGThu6VuZyBraMOhYyBuZ2/DoGkgbcOheSB0w61uaCDEkeG7gyBiw6BuIHbDoCBsYXB0b3AuXG7igJMgR2nhu5tpIHRoaeG7h3UgxJHGsOG7o2MgY8OhYyB0aMOgbmggdOG7sXUgbuG7lWkgYuG6rXQg4bufIG3hu5l0IHPhu5EgbeG7kWMgdGjhu51pIGdpYW4gxJHhu4MgbWluaCBob+G6oSBz4buxIHBow6F0IHRyaeG7g24gY+G7p2EgbmfDoG5oIHRpbiBo4buNYy5cblRow7RuZyBoaeG7g3VcbuKAkyBOw6p1IMSRxrDhu6NjIHbDrSBk4bulIGPhu6UgdGjhu4MgduG7gSB0aGnhur90IGLhu4sgdGjDtG5nIG1pbmguXG7igJMgR2nhuqNpIHRow61jaCDEkcaw4bujYyB2YWkgdHLDsiBj4bunYSBuaOG7r25nIHRoaeG6v3QgYuG7iyB0aMO0bmcgbWluaCDEkeG7kWkgduG7m2kgc+G7sSBwaMOhdCB0cmnhu4NuIGPhu6dhIHjDoyBo4buZaSB2w6AgY3Xhu5ljIGPDoWNoIG3huqFuZyBjw7RuZyBuZ2hp4buHcCA0LjAuXG7igJMgR2nhuqNpIHRow61jaCDEkcaw4bujYyBjw6FjIHRoaeG6v3QgYuG7iyDEkcOzIGPFqW5nIGzDoCBuaOG7r25nIGjhu4cgdGjhu5FuZyB44butIGzDrSB0aMO0bmcgdGluLlxu4oCTIE7DqnUgxJHGsOG7o2MgdsOtIGThu6UgbWluaCBo4buNYSB24buBIG5o4buvbmcgxJHDs25nIGfDs3AgY8ahIGLhuqNuIGPhu6dhIHRpbiBo4buNYyDEkeG7kWkgduG7m2kgeMOjIGjhu5lpLiAiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICI0IChUTikiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIxICjEkFMpIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0KICAgXSwKICAgWwogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiAiY29udGludWUiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjMuIEvEqSBuxINuZyBz4butIGThu6VuZyB0aGnhur90IGLhu4sgc+G7kSBj4bunYSBt4buXaSBjw7RuZyBkw6JuLiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIlx0VuG6rW4gZOG7pW5nXG5cdCDigJMgS2jhu59pIMSR4buZbmcgxJHGsOG7o2MgbeG7mXQgc+G7kSB0aGnhur90IGLhu4sgc+G7kSB0aMO0bmcgZOG7pW5nXG5cdOKAkyBT4butIGThu6VuZyDEkcaw4bujYyBjw6FjIHThu4dwIGThu68gbGnhu4d1LCBjw6FjIGNo4bupYyBuxINuZyB2w6AgcGjhuqduIG3hu4FtIOG7qW5nIGThu6VuZyBjxqEgYuG6o24gY8OgaSBz4bq1biB0csOqbiBjw6FjIHRoaeG6v3QgYuG7iyDEkcOzLiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIiIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9CiAgIF0sCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICIyIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6ICJyZXN0YXJ0IgogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJDaOG7pyDEkeG7gSBCLiBN4bqhbmcgbcOheSB0w61uaCB2w6AgSW50ZXJuZXQiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogInJlc3RhcnQiCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjEuIEtow6FpIG5p4buHbSBt4bqhbmcgbcOheSB0w61uaCwgSW50ZXJuZXQsIElvVC4gUGjDom4gbG/huqFpIG3huqFuZyBtw6F5IHTDrW5oLiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIk5o4bqtbiBiaeG6v3RcbuKAkyBOw6p1IMSRxrDhu6NjIG3hu5l0IHPhu5EgZOG7i2NoIHbhu6UgY+G7pSB0aOG7gyBtw6AgxJBp4buHbiB0b8OhbiDEkcOhbSBtw6J5IGN1bmcgY+G6pXAgY2hvIG5nxrDhu51pIGTDuW5nLlxu4oCTIE7DqnUgxJHGsOG7o2Mga2jDoWkgbmnhu4dtIEludGVybmV0IHbhuqFuIHbhuq10IChJb1QpLlxuVGjDtG5nIGhp4buDdVxu4oCTIFRyw6xuaCBiw6B5IMSRxrDhu6NjIG5o4buvbmcgdGhheSDEkeG7lWkgduG7gSBjaOG6pXQgbMaw4bujbmcgY3Xhu5ljIHPhu5FuZywgcGjGsMahbmcgdGjhu6ljIGjhu41jIHThuq1wIHbDoCBsw6BtIHZp4buHYyB0cm9uZyB4w6MgaOG7mWkgbcOgIOG7nyDEkcOzIG3huqFuZyBtw6F5IHTDrW5oIMSRxrDhu6NjIHPhu60gZOG7pW5nIHBo4buVIGJp4bq/bi4gXG7igJMgU28gc8OhbmggxJHGsOG7o2MgbeG6oW5nIExBTiB2w6AgSW50ZXJuZXQuIFxu4oCTIE7DqnUgxJHGsOG7o2MgdsOtIGThu6UgY+G7pSB0aOG7gyB24buBIHRoYXkgxJHhu5VpIHRyb25nIGN14buZYyBz4buRbmcgbcOgIElvVCDEkWVtIGzhuqFpLiBQaMOhdCBiaeG7g3Ugw70ga2nhur9uIGPDoSBuaMOibiB24buBIGzhu6NpIMOtY2ggY+G7p2EgSW9ULiIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjQgKFROKSIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjEgKMSQUykiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfQogICBdLAogICBbCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6ICJjb250aW51ZSIKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6ICJjb250aW51ZSIKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMi4gU+G7rSBk4bulbmcgZOG7i2NoIHbhu6Ugd2ViLiBU4buxIGLhuqNvIHbhu4cga2hpIHRoYW0gZ2lhIG3huqFuZyIsCiAgICAgInNwYW4iOiAxLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIk5o4bqtbiBiaeG6v3Rcblx04oCTIFRyw6xuaCBiw6B5IMSRxrDhu6NjIHPGoSBsxrDhu6NjIHbhu4EgcGjhuqduIG3hu4FtIMSR4buZYyBo4bqhaS4gXG7igJMgTsOqdSDEkcaw4bujYyBt4buZdCB2w6BpIGPDoWNoIHBow7JuZyB24buHIGtoaSBi4buLIGLhuq90IG7huqF0IHRyw6puIG3huqFuZy5cbuKAkyBOw6p1IMSRxrDhu6NjIG5o4buvbmcgbmd1eSBjxqEgdsOgIHTDoWMgaOG6oWkgbuG6v3UgdGhhbSBnaWEgY8OhYyBob+G6oXQgxJHhu5luZyB0csOqbiBJbnRlcm5ldCBt4buZdCBjw6FjaCBi4bqldCBj4bqpbiB2w6AgdGhp4bq/dSBoaeG7g3UgYmnhur90LlxuVGjDtG5nIGhp4buDdVxuIOKAkyBUcsOsbmggYsOgeSDEkcaw4bujYyBt4buZdCBz4buRIGPDoWNoIMSR4buBIHBow7JuZyBuaOG7r25nIHTDoWMgaOG6oWkga2hpIHRoYW0gZ2lhIGPDoWMgaG/huqF0IMSR4buZbmcgdHLDqm4gSW50ZXJuZXRcblx0VuG6rW4gZOG7pW5nXG5cdOKAkyBT4butIGThu6VuZyDEkcaw4bujYyBt4buZdCBz4buRIGPDtG5nIGPhu6UgdGjDtG5nIGThu6VuZyDEkeG7gyBuZ8SDbiBuZ+G7q2EgdsOgIGxv4bqhaSBi4buPIHBo4bqnbiBt4buBbSDEkeG7mWMgaOG6oWkuXG7igJMgU+G7rSBk4bulbmcgxJHGsOG7o2MgbeG7mXQgc+G7kSBjaOG7qWMgbsSDbmcgeOG7rSBsw60gdGjDtG5nIHRpbiB0csOqbiBtw6F5IFBDIHbDoCB0aGnhur90IGLhu4sgc+G7kSwgdsOtIGThu6UgZOG7i2NoIHThu7EgxJHhu5luZyB2xINuIGLhuqNuIGhheSB0aeG6v25nIG7Ds2kuXG7igJMgS2hhaSB0aMOhYyDEkcaw4bujYyBt4buZdCBz4buRIG5ndeG7k24gaOG7jWMgbGnhu4d1IG3hu58gdHLDqm4gSW50ZXJuZXRcbi0gQmnhur90IGPDoWNoIHThu7EgYuG6o28gduG7hyBk4buvIGxp4buHdSBj4bunYSBjw6EgbmjDom4uIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMiAoVE4pIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMiAoVE4pIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiMSAoVEwpIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiIiwKICAgICAic3BhbiI6IDIsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0KICAgXSwKICAgWwogICAgewogICAgICJ0ZXh0IjogIjMiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJDaOG7pyDEkeG7gSBELiDEkOG6oW8gxJHhu6ljLCBwaMOhcCBsdeG6rXQgdsOgIHbEg24gaG/DoSB0cm9uZyBtw7RpIHRyxrDhu51uZyBz4buRIiwKICAgICAic3BhbiI6IDEsCiAgICAgInZtZXJnZSI6IG51bGwKICAgIH0sCiAgICB7CiAgICAgInRleHQiOiAiTmdoxKlhIHbhu6UgdHXDom4gdGjhu6cgcGjDoXAgbMOtIHRyb25nIG3DtGkgdHLGsOG7nW5nIHPhu5EiLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICJOaOG6rW4gYmnhur90XG7igJMgTsOqdSDEkcaw4bujYyBt4buZdCBz4buRIHbhuqVuIMSR4buBIG7huqN5IHNpbmggduG7gSBwaMOhcCBsdeG6rXQsIMSR4bqhbyDEkeG7qWMsIHbEg24gaG/DoSBraGkgdmnhu4djIGdpYW8gdGnhur9wIHF1YSBt4bqhbmcgdHLhu58gbsOqbiBwaOG7lSBiaeG6v24uXG7igJMgVHLDrG5oIGLDoHkgxJHGsOG7o2MgbeG7mXQgc+G7kSBu4buZaSBkdW5nIGPGoSBi4bqjbiBj4bunYSBMdeG6rXQgQ8O0bmcgbmdo4buHIHRow7RuZyB0aW4sIE5naOG7iyDEkeG7i25oIHbhu4EgcXXhuqNuIGzDrSwgY3VuZyBj4bqlcCwgc+G7rSBk4bulbmcgY8OhYyBz4bqjbiBwaOG6qW0gdsOgIGThu4tjaCB24bulIEPDtG5nIG5naOG7hyB0aMO0bmcgdGluLCBMdeG6rXQgQW4gbmluaCBt4bqhbmcuXG5UaMO0bmcgaGnhu4N1XG4g4oCTIE7DqnUgxJHGsOG7o2MgdsOtIGThu6UgbWluaCBo4buNYSBz4buxIHZpIHBo4bqhbSBi4bqjbiBxdXnhu4FuIHRow7RuZyB0aW4gdsOgIHPhuqNuIHBo4bqpbSBz4buRLiBHaeG6o2kgdGjDrWNoIMSRxrDhu6NjIHPhu7EgdmkgcGjhuqFtIMSRw6MgZGnhu4VuIHJhIG5oxrAgdGjhur8gbsOgbyB2w6AgY8OzIHRo4buDIGThuqtuIHThu5tpIGjhuq11IHF14bqjIGfDrC5cbuKAkyBHaeG6o2kgdGjDrWNoIMSRxrDhu6NjIG3hu5l0IHPhu5EgbuG7mWkgZHVuZyBjxqEgYuG6o24gY+G7p2EgTHXhuq10IEPDtG5nIG5naOG7hyB0aMO0bmcgdGluLCBOZ2jhu4sgxJHhu4tuaCB24buBIHF14bqjbiBsw60sIGN1bmcgY+G6pXAsIHPhu60gZOG7pW5nIGPDoWMgc+G6o24gcGjhuqltIHbDoCBk4buLY2ggduG7pSBDw7RuZyBuZ2jhu4cgdGjDtG5nIHRpbiwgTHXhuq10IEFuIG5pbmggbeG6oW5nLiAgTsOqdSDEkcaw4bujYyB2w60gZOG7pSBtaW5oIGjhu41hLlxu4oCTIEdp4bqjaSB0aMOtY2ggxJHGsOG7o2MgbeG7mXQgc+G7kSBraMOtYSBj4bqhbmggcGjDoXAgbMOtIGPhu6dhIHbhuqVuIMSR4buBIGLhuqNuIHF1eeG7gW4sIGPhu6dhIHZp4buHYyBz4bufIGjhu691LCBz4butIGThu6VuZyB2w6AgdHJhbyDEkeG7lWkgdGjDtG5nIHRpbiB0cm9uZyBtw7RpIHRyxrDhu51uZyBz4buRLiBOw6p1IMSRxrDhu6NjIHbDrSBk4bulIG1pbmggaG/huqEuXG7igJMgTsOqdSDEkcaw4bujYyB2w60gZOG7pSB24buBIG5o4buvbmcgdMOhYyBo4bqhaSBj4bunYSB2aeG7h2MgY2hpYSBz4bq7IHbDoCBwaOG7lSBiaeG6v24gdGjDtG5nIHRpbiBt4buZdCBjw6FjaCBi4bqldCBj4bqpbi5cbuKAkyBOw6p1IMSRxrDhu6NjIG3hu5l0IHbDoGkgYmnhu4duIHBow6FwIMSRxqFuIGdp4bqjbiB2w6AgdGjDtG5nIGThu6VuZyDEkeG7gyBuw6JuZyBjYW8gdMOtbmggYW4gdG/DoG4gdsOgIGjhu6NwIHBow6FwIGPhu6dhIHZp4buHYyBjaGlhIHPhursgdGjDtG5nIHRpbiB0cm9uZyBtw7RpIHRyxrDhu51uZyBz4buRLlxuVuG6rW4gZOG7pW5nXG7igJMgVuG6rW4gZOG7pW5nIMSRxrDhu6NjIEx14bqtdCB2w6AgTmdo4buLIMSR4buLbmggbsOqdSB0csOqbiDEkeG7gyB4w6FjIMSR4buLbmggxJHGsOG7o2MgdMOtbmggaOG7o3AgcGjDoXAgY+G7p2EgbeG7mXQgaMOgbmggdmkgbsOgbyDEkcOzIHRyb25nIGzEqW5oIHbhu7FjIHF14bqjbiBsw60sIGN1bmcgY+G6pXAsIHPhu60gZOG7pW5nIGPDoWMgc+G6o24gcGjhuqltIHbDoCBk4buLY2ggduG7pSBDw7RuZyBuZ2jhu4cgdGjDtG5nIHRpbi4iLAogICAgICJzcGFuIjogMSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICI0IChUTikiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIiLAogICAgICJzcGFuIjogMiwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIxKFRMKSIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9CiAgIF0sCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICJU4buJIGzhu4cgJSIsCiAgICAgInNwYW4iOiA1LAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjQwJSIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjMwJSIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjIwJSIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9LAogICAgewogICAgICJ0ZXh0IjogIjEwJSIsCiAgICAgInNwYW4iOiAyLAogICAgICJ2bWVyZ2UiOiBudWxsCiAgICB9CiAgIF0sCiAgIFsKICAgIHsKICAgICAidGV4dCI6ICJU4buJIGzhu4cgY2h1bmciLAogICAgICJzcGFuIjogNSwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICI3MCUiLAogICAgICJzcGFuIjogNCwKICAgICAidm1lcmdlIjogbnVsbAogICAgfSwKICAgIHsKICAgICAidGV4dCI6ICIzMCUiLAogICAgICJzcGFuIjogNCwKICAgICAidm1lcmdlIjogbnVsbAogICAgfQogICBdCiAgXQogfSwKIHsKICAidHlwZSI6ICJwIiwKICAidGV4dCI6ICIiCiB9LAogewogICJ0eXBlIjogInAiLAogICJ0ZXh0IjogIiIKIH0sCiB7CiAgInR5cGUiOiAicCIsCiAgInRleHQiOiAiIgogfSwKIHsKICAidHlwZSI6ICJzZWN0UHIiCiB9Cl0K"
).decode("utf-8"))

# --------------------------------------------------------------------------
# 2. Font & mau sac
# --------------------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DV", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DV-B", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("DV-I", os.path.join(FONT_DIR, "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont("DV-BI", os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("DVM", os.path.join(FONT_DIR, "DejaVuSansMono.ttf")))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV-I", boldItalic="DV-BI")

NAVY   = colors.HexColor("#17365D")
BLUE   = colors.HexColor("#1D4ED8")
TEAL   = colors.HexColor("#0F766E")
AMBER  = colors.HexColor("#B45309")
RED    = colors.HexColor("#B91C1C")
GRAY   = colors.HexColor("#475569")
LGRAY  = colors.HexColor("#94A3B8")
BG     = colors.HexColor("#F1F5F9")
BGTEAL = colors.HexColor("#ECFDF5")
BGAMB  = colors.HexColor("#FFF7ED")
BGBLUE = colors.HexColor("#EFF6FF")
WHITE  = colors.white
LINE   = colors.HexColor("#CBD5E1")

# --------------------------------------------------------------------------
# 3. Styles
# --------------------------------------------------------------------------
def S(name, **kw):
    kw.setdefault("fontName", "DV")
    kw.setdefault("fontSize", 9.3)
    kw.setdefault("leading", 13.6)
    kw.setdefault("textColor", colors.HexColor("#1E293B"))
    return ParagraphStyle(name, **kw)

ST = {
    "title":    S("title", fontName="DV-B", fontSize=25, leading=31, textColor=NAVY, alignment=TA_CENTER),
    "subtitle": S("subtitle", fontName="DV-B", fontSize=13.5, leading=19, textColor=TEAL, alignment=TA_CENTER),
    "cover":    S("cover", fontSize=10.5, leading=17, alignment=TA_CENTER, textColor=GRAY),
    "h1t":      S("h1t", fontName="DV-B", fontSize=15, leading=20, textColor=WHITE,
                   backColor=NAVY, borderPadding=(9, 9, 9, 9), spaceBefore=13, spaceAfter=9),
    "h2":       S("h2", fontName="DV-B", fontSize=12.5, leading=17, textColor=TEAL, spaceBefore=11, spaceAfter=5),
    "h3":       S("h3", fontName="DV-B", fontSize=10.6, leading=15, textColor=NAVY, spaceBefore=8, spaceAfter=3),
    "h4":       S("h4", fontName="DV-B", fontSize=9.8, leading=14, textColor=AMBER, spaceBefore=6, spaceAfter=2),
    "body":     S("body", alignment=TA_JUSTIFY, spaceAfter=5),
    "bodyc":    S("bodyc", alignment=TA_CENTER, spaceAfter=4),
    "bullet":   S("bullet", alignment=TA_JUSTIFY, leftIndent=11, bulletIndent=2, spaceAfter=2.6),
    "bullet2":  S("bullet2", leftIndent=22, bulletIndent=12, spaceAfter=2, fontSize=9.0, leading=13),
    "q":        S("q", fontName="DV-B", fontSize=9.5, leading=14, textColor=NAVY),
    "a":        S("a", fontSize=9.2, leading=13.4, alignment=TA_JUSTIFY),
    "tiny":     S("tiny", fontSize=8.0, leading=11.2, textColor=GRAY),
    "tinyj":    S("tinyj", fontSize=8.0, leading=11.2, alignment=TA_JUSTIFY),
    "cell":     S("cell", fontSize=8.2, leading=11.2),
    "cellb":    S("cellb", fontName="DV-B", fontSize=8.2, leading=11.2),
    "cellsm":   S("cellsm", fontSize=6.6, leading=8.6),
    "cellsmb":  S("cellsmb", fontName="DV-B", fontSize=6.6, leading=8.6),
    "th":       S("th", fontName="DV-B", fontSize=8.3, leading=11.4, textColor=WHITE),
    "thsm":     S("thsm", fontName="DV-B", fontSize=6.5, leading=8.6, textColor=WHITE, alignment=TA_CENTER),
    "thtiny":   S("thtiny", fontName="DV-B", fontSize=5.7, leading=7.4, textColor=WHITE, alignment=TA_CENTER),
    "celltiny": S("celltiny", fontSize=6.1, leading=8.0),
    "opt":      S("opt", fontSize=9.0, leading=13, leftIndent=8, spaceAfter=1),
    "note":     S("note", fontSize=9.0, leading=13.2, alignment=TA_JUSTIFY),
    "toc0":     S("toc0", fontName="DV-B", fontSize=10.2, leading=17, textColor=NAVY, spaceBefore=5),
    "toc1":     S("toc1", fontSize=9.3, leading=15, leftIndent=13),
    "toc2":     S("toc2", fontSize=8.8, leading=13.5, leftIndent=27, textColor=GRAY),
}

# --------------------------------------------------------------------------
# 4. Ham tien ich
# --------------------------------------------------------------------------
_MARKUP_TOKENS = [
    ("<b>", "\x01B1\x01"), ("</b>", "\x01B0\x01"),
    ("<i>", "\x01I1\x01"), ("</i>", "\x01I0\x01"),
    ("<br/>", "\x01BR\x01"), ("<br>", "\x01BR\x01"),
    ("<super>", "\x01SU1\x01"), ("</super>", "\x01SU0\x01"),
]

def esc(s):
    """Escape ky tu dac biet cho Paragraph (giu nguyen dau tieng Viet)."""
    s = str(s)
    for tag, token in _MARKUP_TOKENS:
        s = s.replace(tag, token)
    s = html.escape(s, quote=False).replace("\n", "<br/>")
    for tag, token in _MARKUP_TOKENS:
        s = s.replace(token, tag)
    return s

def P(text, style="body", raw=False):
    return Paragraph(text if raw else esc(text), ST[style] if isinstance(style, str) else style)

def B(text, style="bullet", bullet="•", raw=False):
    t = text if raw else esc(text)
    return Paragraph(t, ST[style] if isinstance(style, str) else style, bulletText=bullet)

def RULE(color=LINE, thick=0.8, before=3, after=6):
    t = Table([[""]], colWidths=[465], rowHeights=[0.3])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), thick, color),
                           ("TOPPADDING", (0, 0), (-1, -1), before),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), after),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    return t

def BOX(flowables, bg=BG, border=LINE, width=465, pad=8, leftbar=None):
    t = Table([[flowables]], colWidths=[width])
    cmds = [("BACKGROUND", (0, 0), (-1, -1), bg),
            ("BOX", (0, 0), (-1, -1), 0.7, border),
            ("LEFTPADDING", (0, 0), (-1, -1), pad),
            ("RIGHTPADDING", (0, 0), (-1, -1), pad),
            ("TOPPADDING", (0, 0), (-1, -1), pad - 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), pad - 2)]
    if leftbar:
        cmds.append(("LINEBEFORE", (0, 0), (0, -1), 3.2, leftbar))
    t.setStyle(TableStyle(cmds))
    return t

def H1(num, text):
    return Paragraph(esc(num + "  " + text), ST["h1t"])

def H2(text):
    return Paragraph(esc(text), ST["h2"])

def H3(text):
    return Paragraph(esc(text), ST["h3"])

def H4(text):
    return Paragraph(esc(text), ST["h4"])

def TB(data, widths, header=True, font="cell", aligns=None, zebra=True, span_cmds=None, hbg=NAVY):
    """Tao bang voi header dam nen xanh, ke vien nhat, co the truyen SPAN."""
    body = []
    for r_i, row in enumerate(data):
        rr = []
        for cell in row:
            if isinstance(cell, Paragraph):
                rr.append(cell)
            else:
                sty = "th" if (header and r_i == 0 and font == "cell") else (
                      "thsm" if (header and r_i == 0) else font)
                rr.append(Paragraph(esc(cell), ST[sty]))
        body.append(rr)
    t = Table(body, colWidths=widths, repeatRows=1 if header else 0)
    cmds = [("GRID", (0, 0), (-1, -1), 0.45, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5)]
    if header:
        cmds.append(("BACKGROUND", (0, 0), (-1, 0), hbg))
    if zebra:
        for i in range(1 if header else 0, len(body)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F8FAFC")))
    if aligns:
        for col, al in aligns.items():
            cmds.append(("ALIGN", (col, 0), (col, -1), al))
    if span_cmds:
        cmds.extend(span_cmds)
    t.setStyle(TableStyle(cmds))
    return t

def QA(code, question, answer, level=""):
    """Khoi cau hoi - dap an mau."""
    head = Paragraph(
        '<font color="#0F766E"><b>' + esc(code) + "</b></font>" +
        (('  <font color="#94A3B8" size="7.5">[' + esc(level) + "]</font>") if level else "") +
        "  " + esc(question), ST["q"])
    ans = Paragraph('<font color="#B45309"><b>Đáp án:</b></font> ' + esc(answer), ST["a"])
    inner = [[head], [ans]]
    t = Table(inner, colWidths=[451])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), BGBLUE),
        ("BACKGROUND", (0, 1), (0, 1), BGAMB),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t

def MCQ(code, question, options, answer, explain="", compact=True):
    """Cau trac nghiem 4 lua chon co dap an + giai thich."""
    parts = [Paragraph('<font color="#17365D"><b>' + esc(code) + ".</b></font> " + esc(question), ST["q"])]
    if compact:
        line = "   ".join("<b>" + k + ".</b> " + esc(v) for k, v in options.items())
        parts.append(Paragraph(line, ST["opt"]))
    else:
        for k, v in options.items():
            parts.append(Paragraph("<b>" + k + ".</b> " + esc(v), ST["opt"]))
    tail = '<font color="#B45309"><b>Đáp án: ' + esc(answer) + "</b></font>"
    if explain:
        tail += " — " + esc(explain)
    parts.append(Paragraph(tail, ST["tinyj"]))
    t = Table([[parts]], colWidths=[465])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#E2E8F0")),
                           ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FCFDFE")),
                           ("LEFTPADDING", (0, 0), (-1, -1), 7),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                           ("TOPPADDING", (0, 0), (-1, -1), 5),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return t

def TFQ(code, stem, statements, answers, explain=""):
    """Cau dung/sai: statements = [(nhan, noidung)], answers = 'DDSS'..."""
    parts = [Paragraph('<font color="#17365D"><b>' + esc(code) + ".</b></font> " + esc(stem), ST["q"])]
    for label, txt in statements:
        parts.append(Paragraph("<b>" + esc(label) + ")</b> " + esc(txt), ST["opt"]))
    keys = {"Đ": "Đúng", "D": "Đúng", "S": "Sai"}
    res = ", ".join(labels + ") " + keys[a] for (labels, _), a in zip(statements, answers))
    tail = '<font color="#B45309"><b>Đáp án:</b></font> ' + esc(res)
    if explain:
        tail += ". " + esc(explain)
    parts.append(Paragraph(tail, ST["tinyj"]))
    t = Table([[parts]], colWidths=[465])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#E2E8F0")),
                           ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FCFDFE")),
                           ("LEFTPADDING", (0, 0), (-1, -1), 7),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                           ("TOPPADDING", (0, 0), (-1, -1), 5),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return t

story = []

# ==========================================================================
# TRANG BIA
# ==========================================================================
story.append(Spacer(1, 26*mm))
cover_band = Table([[""]], colWidths=[465], rowHeights=[6])
cover_band.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TEAL)]))
story.append(cover_band)
story.append(Spacer(1, 10*mm))
story.append(P("ĐỀ CƯƠNG ÔN TẬP", "title"))
story.append(P("KIỂM TRA GIỮA KÌ I", "title"))
story.append(Spacer(1, 5*mm))
story.append(P("MÔN TIN HỌC 10 – ĐỊNH HƯỚNG ICT", "subtitle"))
story.append(P("Theo bộ sách giáo khoa KẾT NỐI TRI THỨC VỚI CUỘC SỐNG", "cover"))
story.append(Spacer(1, 8*mm))

cover_info = [
    ["Thời gian làm bài", "45 phút"],
    ["Hình thức kiểm tra", "Kết hợp trắc nghiệm (70%) và tự luận (30%)"],
    ["Phạm vi kiến thức", "Chủ đề A – Máy tính và xã hội tri thức; Chủ đề B – Mạng máy tính và Internet; Chủ đề D – Đạo đức, pháp luật và văn hoá trong môi trường số"],
    ["Căn cứ biên soạn", "Ma trận đề kiểm tra giữa kì I và Đặc tả đề kiểm tra giữa kì I (tệp MA TRAN GIUA KI I - LOP 10.docx)"],
    ["Cấu trúc tài liệu", "7 phần chính + 2 phụ lục; toàn bộ câu hỏi và đáp án của tài liệu gốc được giữ nguyên và phát triển"],
]
t = Table([[Paragraph("<b>" + esc(a) + "</b>", ST["cell"]), Paragraph(esc(b), ST["cell"])] for a, b in cover_info],
          colWidths=[110, 355])
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, LINE),
                       ("BACKGROUND", (0, 0), (0, -1), BG),
                       ("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("LEFTPADDING", (0, 0), (-1, -1), 7),
                       ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                       ("TOPPADDING", (0, 0), (-1, -1), 6),
                       ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story.append(t)
story.append(Spacer(1, 9*mm))
story.append(BOX([P("Tài liệu được biên soạn công phu theo nguyên tắc: <b>học tới đâu – hỏi tới đó – có đáp án ngay tại đó</b>. "
                    "Mỗi yêu cầu cần đạt trong bản đặc tả đều trở thành một câu hỏi kèm đáp án mẫu (Phần IV). "
                    "Phần V, VI cung cấp thêm ngân hàng câu hỏi và đề thi thử đúng cấu trúc ma trận.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(Spacer(1, 6*mm))
story.append(P("Biên soạn: tháng 10 năm 2026  •  Dùng cho học sinh lớp 10", "cover"))
story.append(PageBreak())

# ==========================================================================
# MUC LUC
# ==========================================================================
story.append(H1("MỤC", "LỤC TÀI LIỆU"))
toc = TableOfContents()
toc.levelStyles = [ST["toc0"], ST["toc1"], ST["toc2"]]
story.append(toc)
story.append(PageBreak())

# ==========================================================================
# LOI NOI DAU
# ==========================================================================
story.append(H1("LỜI NÓI ĐẦU", "CĂN CỨ VÀ CÁCH SỬ DỤNG ĐỀ CƯƠNG"))
story.append(H2("1. Căn cứ biên soạn"))
story.append(P("Đề cương này được biên soạn từ tệp <b>«MA TRẬN GIUA KI I - LOP 10.docx»</b> – văn bản gồm hai phần: "
               "<b>Ma trận đề kiểm tra giữa kì I</b> (bảng phân bổ câu hỏi theo chủ đề và mức độ nhận thức) và "
               "<b>Đặc tả đề kiểm tra giữa kì I</b> (bảng mô tả chi tiết yêu cầu cần đạt). Nội dung kiến thức được trình bày "
               "theo bộ sách <b>Tin học 10 – Kết nối tri thức với cuộc sống</b>, đồng thời bổ sung đầy đủ các thuật ngữ mà bản đặc tả yêu cầu."))
story.append(BOX([
    P("<b>Lưu ý quan trọng về «câu hỏi và đáp án có trong tài liệu gốc».</b> Tài liệu gốc là một bảng ma trận – đặc tả đề, "
      "không phải một đề thi có sẵn câu hỏi – đáp án. Vì vậy, để không bỏ sót bất kì nội dung nào, đề cương thực hiện ba việc:", "note"),
    B("Giữ <b>nguyên văn 100% văn bản gốc</b> (các dòng thông tin chung, hai bảng ma trận và đặc tả) tại <b>Phụ lục A</b>.", "bullet"),
    B("Chuyển <b>toàn bộ 35 yêu cầu cần đạt</b> trong bản đặc tả thành 35 câu hỏi có đáp án mẫu tại <b>Phần IV</b>, "
      "đánh mã A1-NB-1 … D-VDC-1 để dễ tra cứu.", "bullet"),
    B("Bổ sung <b>ngân hàng 60 câu trắc nghiệm, 8 câu đúng/sai, 15 câu tự luận</b> (Phần V) và "
      "<b>01 đề thi thử đúng cấu trúc</b> (Phần VI), tất cả đều có đáp án và giải thích.", "bullet"),
    B("<b>Phụ lục B</b> là bảng đối chiếu 35 yêu cầu cần đạt → vị trí kiến thức → câu hỏi – đáp án → câu luyện tập, "
      "giúp kiểm chứng độ bao phủ 100%.", "bullet"),
], bg=BGBLUE, border=BLUE, leftbar=BLUE))
story.append(H2("2. Đối chiếu tên chủ đề giữa ma trận và sách giáo khoa"))
story.append(P("Ma trận dùng nhãn <b>Chủ đề A – B – D</b> theo Chương trình GDPT 2018 (định hướng ICT); sách "
               "<b>Kết nối tri thức</b> dùng nhãn <b>Chủ đề 1 – 2 – 3</b>. Bảng dưới đây giúp bạn tìm đúng bài học trong SGK. "
               "Đây chỉ là đổi tên gọi; nội dung kiến thức là tương đương."))
story.append(TB([
    ["Trong ma trận", "Trong SGK Kết nối tri thức", "Nội dung chính"],
    ["Chủ đề A. Máy tính và xã hội tri thức", "Chủ đề 1, Bài 1, 2 và Bài 7 (thực hành thiết bị số)", "Dữ liệu – thông tin – xử lí thông tin; đơn vị lưu trữ; thiết bị thông minh; thành tựu tin học; kĩ năng sử dụng thiết bị số"],
    ["Chủ đề B. Mạng máy tính và Internet", "Chủ đề 2, Bài 8, 9, 10", "LAN và Internet; điện toán đám mây; IoT; dịch vụ web; học liệu mở; an toàn trên không gian mạng"],
    ["Chủ đề D. Đạo đức, pháp luật và văn hoá trong môi trường số", "Chủ đề 3, Bài 11", "Bản quyền; Luật CNTT; Luật An ninh mạng; Nghị định 72/2013; chia sẻ thông tin an toàn, hợp pháp"],
], [128, 145, 192]))
story.append(P("Một số nội dung trong bản đặc tả (điện toán đám mây, IoT, Luật Công nghệ thông tin, Nghị định 72/2013/NĐ-CP, "
               "Luật An ninh mạng, bản quyền số) được trình bày đầy đủ trong Phần II vì chúng là yêu cầu kiểm tra, dù SGK "
               "Kết nối tri thức có cách tiếp cận hơi khác.", "tinyj"))
story.append(H2("3. Cách sử dụng đề cương hiệu quả"))
for x in [
    "Bước 1 – Đọc Phần I để biết đề gồm bao nhiêu câu, mỗi phần bao nhiêu điểm, chủ đề nào chiếm tỉ trọng cao nhất.",
    "Bước 2 – Học Phần II theo thứ tự A → B → D; mỗi tiết kết thúc bằng khung «Ghi nhớ nhanh».",
    "Bước 3 – Xem Phần III (bảng tra cứu nhanh) ngay trước khi làm bài để nhớ công thức đổi đơn vị, bảng luật và các bảng so sánh.",
    "Bước 4 – Tự trả lời 35 câu hỏi ở Phần IV; đối chiếu với đáp án mẫu. Đây chính là toàn bộ yêu cầu cần đạt của bản đặc tả.",
    "Bước 5 – Luyện tập Phần V, sau đó làm đề thi thử Phần VI trong đúng 45 phút và tự chấm theo thang điểm.",
    "Bước 6 – Cuối cùng, đọc Phần VII (mẹo làm bài) và kiểm tra lại Phụ lục B để chắc chắn không còn ý nào chưa ôn.",
]:
    story.append(B(x))
story.append(PageBreak())

# ==========================================================================
# PHAN I - CAU TRUC DE & MA TRAN
# ==========================================================================
story.append(H1("PHẦN I", "CẤU TRÚC ĐỀ KIỂM TRA VÀ MA TRẬN ĐỀ"))
story.append(H2("I.1. Thông tin chung về đề kiểm tra (nguyên văn tài liệu gốc)"))
intro_lines = [it["text"] for it in SOURCE_DATA if it["type"] == "p" and it["text"].strip()]
for line in intro_lines:
    if line.startswith("MA TRẬN") or line.startswith("MÔN:"):
        continue
    story.append(B(line, "bullet", bullet="–" if line.startswith("-") else "+"))
story.append(P("Như vậy, đề gồm <b>22 câu trắc nghiệm</b> (20 câu 4 lựa chọn + 2 câu đúng/sai) và <b>3 câu tự luận</b>. "
               "Tổng điểm 10, trong đó 7,0 điểm trắc nghiệm và 3,0 điểm tự luận.", "note"))

story.append(H2("I.2. Ma trận đề (bản trình bày lại để dễ đọc)"))
story.append(P("Bảng dưới đây giữ nguyên toàn bộ số liệu của ma trận gốc nhưng gom các cột con cho dễ nhìn. "
               "Bản nguyên văn 18 cột được đặt tại <b>Phụ lục A.2</b>.", "tinyj"))
story.append(TB([
    ["TT", "Chủ đề / Đơn vị kiến thức", "Nhận biết", "Thông hiểu", "Vận dụng", "Vận dụng cao", "Tổng"],
    ["1", "Chủ đề A. Máy tính và xã hội tri thức", "", "", "", "", "40% (4,0 đ)"],
    ["", "A1. Dữ liệu, thông tin và xử lý thông tin", "2 TN", "2 TN", "1 TL", "–", "20% (2,0 đ)"],
    ["", "A2. Vai trò của máy tính và thiết bị thông minh", "4 TN", "2 ý ĐS", "2 ý ĐS", "–", "20% (2,0 đ)"],
    ["", "A3. Kĩ năng sử dụng thiết bị số của mỗi công dân", "–", "–", "–", "–", ""],
    ["2", "Chủ đề B. Mạng máy tính và Internet", "", "", "", "", "40% (4,0 đ)"],
    ["", "B1. Khái niệm mạng máy tính, Internet, IoT. Phân loại mạng", "4 TN", "2 ý ĐS", "2 ý ĐS", "–", "20% (2,0 đ)"],
    ["", "B2. Sử dụng dịch vụ web. Tự bảo vệ khi tham gia mạng", "4 TN", "1 TL", "1 TL", "–", "20% (2,0 đ)"],
    ["3", "Chủ đề D. Đạo đức, pháp luật và văn hoá trong môi trường số", "", "", "", "", "20% (2,0 đ)"],
    ["", "D1. Nghĩa vụ tuân thủ pháp lí trong môi trường số", "2 TN", "2 TN", "–", "1 TL", "20% (2,0 đ)"],
    ["TỔNG", "16 câu TN nhận biết · 4 câu TN thông hiểu · 4 ý ĐS · 1 TL thông hiểu · 4 ý ĐS vận dụng · 1 TL vận dụng · 1 TL vận dụng cao", "", "", "", "", "10 điểm"],
], [24, 190, 45, 47, 45, 45, 69], font="cellsm"))
story.append(BOX([
    P("<b>Đọc ma trận:</b> «TN» = trắc nghiệm 4 lựa chọn (0,25 điểm/câu); «ĐS» = câu lựa chọn đúng/sai "
      "(1,0 điểm/câu, mỗi câu có 4 ý); «TL» = tự luận (1,0 điểm/câu). Chủ đề A chiếm 40%, B chiếm 40%, D chiếm 20%. "
      "Năm đơn vị A1, A2, B1, B2, D1 mỗi đơn vị 20% (2,0 điểm). Tỉ lệ chung: 70% trắc nghiệm – 30% tự luận.", "note"),
    P("<b>Mức độ nhận thức:</b> Nhận biết 40% – Thông hiểu 30% – Vận dụng 20% – Vận dụng cao 10%. "
      "Câu hỏi dễ nhất tập trung ở mức Nhận biết; câu khó nhất là 1 câu tự luận Vận dụng cao ở Chủ đề D.", "note"),
], bg=BGAMB, border=AMBER, leftbar=AMBER))

story.append(H2("I.3. Đặc tả đề – toàn bộ yêu cầu cần đạt (nguyên văn, trình bày theo đơn vị)"))
spec_rows = [
    ["A1. Dữ liệu, thông tin và xử lý thông tin", "Nhận biết", "Nêu được sự ưu việt của việc lưu trữ dựa trên các thiết bị số.", "2 TN"],
    ["", "Thông hiểu", "Phân biệt được thông tin và dữ liệu; nêu được ví dụ minh hoạ về thông tin và dữ liệu.", "2 TN"],
    ["", "Vận dụng", "Chuyển đổi được giữa các đơn vị lưu trữ thông tin: B, KB, MB,…; xử lí và truyền thông tin bằng thiết bị số.", "1 TL"],
    ["A2. Vai trò của máy tính và thiết bị thông minh", "Nhận biết", "Trình bày được những đóng góp cơ bản của tin học đối với xã hội; nhận biết được một vài thiết bị số thông dụng khác ngoài máy tính để bàn và laptop; giới thiệu được các thành tựu nổi bật ở một số mốc thời gian minh hoạ sự phát triển của ngành tin học.", "4 TN"],
    ["", "Thông hiểu", "Nêu được ví dụ cụ thể về thiết bị thông minh; giải thích được vai trò của thiết bị thông minh với xã hội và CMCN 4.0; giải thích được các thiết bị đó cũng là hệ thống xử lí thông tin; nêu ví dụ về đóng góp của tin học với xã hội.", "1 ĐS (2 ý)"],
    ["A3. Kĩ năng sử dụng thiết bị số", "Vận dụng", "Khởi động được một số thiết bị số thông dụng; sử dụng được các tệp dữ liệu, các chức năng và phần mềm ứng dụng cơ bản cài sẵn trên các thiết bị đó.", "(kĩ năng)"],
    ["B1. Mạng máy tính, Internet, IoT. Phân loại mạng", "Nhận biết", "Nêu được một số dịch vụ cụ thể mà Điện toán đám mây cung cấp cho người dùng; nêu được khái niệm Internet vạn vật (IoT).", "4 TN"],
    ["", "Thông hiểu", "Trình bày được những thay đổi về chất lượng cuộc sống, phương thức học tập và làm việc khi mạng máy tính phổ biến; so sánh được mạng LAN và Internet; nêu ví dụ về thay đổi do IoT đem lại và phát biểu ý kiến cá nhân về lợi ích của IoT.", "1 ĐS (2 ý)"],
    ["B2. Sử dụng dịch vụ web. Tự bảo vệ khi tham gia mạng", "Nhận biết", "Trình bày được sơ lược về phần mềm độc hại; nêu được một vài cách phòng vệ khi bị bắt nạt trên mạng; nêu được những nguy cơ và tác hại nếu tham gia Internet bất cẩn, thiếu hiểu biết.", "2 TN"],
    ["", "Thông hiểu", "Trình bày được một số cách đề phòng những tác hại khi tham gia các hoạt động trên Internet.", "2 TN"],
    ["", "Vận dụng", "Sử dụng được công cụ ngăn ngừa và loại bỏ phần mềm độc hại; sử dụng được chức năng xử lí thông tin trên PC và thiết bị số (dịch tự động văn bản, tiếng nói); khai thác được học liệu mở trên Internet; biết cách tự bảo vệ dữ liệu cá nhân.", "1 TL"],
    ["D1. Nghĩa vụ tuân thủ pháp lí trong môi trường số", "Nhận biết", "Nêu được một số vấn đề nảy sinh về pháp luật, đạo đức, văn hoá khi giao tiếp qua mạng phổ biến; trình bày được một số nội dung cơ bản của Luật Công nghệ thông tin, Nghị định về quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ CNTT, Luật An ninh mạng.", "2 TN + 2 TN"],
    ["", "Thông hiểu", "Nêu ví dụ vi phạm bản quyền thông tin và sản phẩm số, giải thích diễn biến và hậu quả; giải thích nội dung cơ bản của các luật/nghị định kèm ví dụ; giải thích khía cạnh pháp lí của bản quyền, sở hữu, sử dụng và trao đổi thông tin số kèm ví dụ; nêu ví dụ tác hại của chia sẻ, phổ biến thông tin bất cẩn; nêu biện pháp đơn giản, thông dụng nâng cao tính an toàn và hợp pháp khi chia sẻ thông tin.", "(TL/ĐS)"],
    ["", "Vận dụng cao", "Vận dụng Luật và Nghị định để xác định tính hợp pháp của một hành vi trong lĩnh vực quản lí, cung cấp, sử dụng sản phẩm và dịch vụ CNTT.", "1 TL"],
]
story.append(TB([["Đơn vị kiến thức / kĩ năng", "Mức độ", "Yêu cầu cần kiểm tra, đánh giá (nguyên văn)", "Số câu"]] + spec_rows,
                [105, 47, 265, 48], font="cellsm"))
story.append(P("Bảng trên là bản đọc của bảng đặc tả gốc. Từng dòng yêu cầu được đánh mã và chuyển thành câu hỏi có đáp án ở "
               "<b>Phần IV</b>; bản nguyên văn 12 cột của bảng đặc tả được giữ tại <b>Phụ lục A.3</b>.", "tinyj"))
story.append(PageBreak())

# ==========================================================================
# PHAN II - HE THONG KIEN THUC TRONG TAM
# ==========================================================================
story.append(H1("PHẦN II", "HỆ THỐNG KIẾN THỨC TRỌNG TÂM"))
story.append(P("Phần này hệ thống lại toàn bộ chương trình giữa kì I theo đúng 3 chủ đề của ma trận. "
               "Mỗi mục bắt đầu bằng <b>yêu cầu cần đạt</b> (trích từ bản đặc tả), tiếp theo là kiến thức cốt lõi, "
               "bảng so sánh, ví dụ và kết thúc bằng khung <b>Ghi nhớ nhanh</b>."))

# ---- II.1 CHU DE A -------------------------------------------------------
story.append(H2("II.1. Chủ đề A. Máy tính và xã hội tri thức"))
story.append(H3("II.1.1. Dữ liệu, thông tin và xử lý thông tin"))
story.append(BOX([P("<b>Yêu cầu cần đạt:</b> Nêu được sự ưu việt của việc lưu trữ dựa trên thiết bị số. "
                    "Phân biệt được thông tin và dữ liệu; nêu được ví dụ minh hoạ. "
                    "Chuyển đổi được giữa các đơn vị lưu trữ thông tin B, KB, MB,…; xử lí và truyền thông tin bằng thiết bị số.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(H4("a) Hai khái niệm nền tảng"))
story.append(TB([
    ["Khái niệm", "Định nghĩa", "Ví dụ"],
    ["Thông tin", "Tất cả những gì mang lại cho con người sự hiểu biết, gắn liền với quá trình nhận thức. Thông tin có thể làm thay đổi hành động của con người.", "Biết được «ngày mai trời mưa to» → mang theo ô; biết điểm kiểm tra Tin học đạt 9 → vui mừng."],
    ["Dữ liệu", "Thông tin đã được đưa vào máy tính, được biểu diễn dưới dạng văn bản, số, hình ảnh, âm thanh, video… để máy tính nhận biết, lưu trữ và xử lí được.", "Tệp «diem.docx» chứa các con số 8; 9; 10; tệp «anh.jpg» chứa bức ảnh; tệp «nhac.mp3»."],
], [78, 205, 182]))
story.append(P("<b>Quan hệ:</b> dữ liệu là «vật liệu thô», thông tin là «ý nghĩa» rút ra được sau khi xử lí dữ liệu. "
               "Cùng một dữ liệu có thể cho những thông tin khác nhau với những người khác nhau, tuỳ vào hiểu biết của mỗi người. "
               "Trong máy tính, <b>xử lí thông tin chính là xử lí dữ liệu</b>."))
story.append(B("Ví dụ phân biệt: dãy số <b>37; 39; 40; 38; 41</b> là dữ liệu. Sau khi xử lí (tính trung bình, so sánh với ngưỡng), "
               "ta có thông tin: «nhiệt độ cơ thể 39 °C – bạn đang bị sốt cao, cần đến bác sĩ».", "bullet"))
story.append(H4("b) Quá trình xử lí thông tin của máy tính (3 bước)"))
story.append(TB([
    ["Bước", "Tên gọi", "Hoạt động", "Thiết bị tương ứng"],
    ["1", "Tiếp nhận dữ liệu (vào)", "Thu nhận tín hiệu từ thế giới xung quanh, chuyển thành dữ liệu số.", "Bàn phím, chuột, micro, camera, máy quét, cảm biến nhiệt độ…"],
    ["2", "Xử lí dữ liệu", "Tính toán, so sánh, phân loại, lưu trữ, mã hoá… theo chương trình.", "CPU, bộ nhớ RAM, ổ cứng, phần mềm ứng dụng"],
    ["3", "Đưa ra kết quả (ra)", "Xuất kết quả dưới dạng con người nghe, nhìn, hiểu được; đồng thời có thể lưu thành tệp và truyền đi.", "Màn hình, loa, máy in, tệp dữ liệu, đường truyền mạng"],
], [30, 92, 180, 163], font="cell"))
story.append(P("Ví dụ hoàn chỉnh: bạn nói câu «Xin chào» vào điện thoại (bước 1 – micro thu âm) → ứng dụng nhận dạng giọng nói "
               "chuyển thành văn bản (bước 2) → màn hình hiện chữ «Xin chào» và tệp âm thanh được gửi qua Zalo (bước 3)."))
story.append(H4("c) Sự ưu việt của việc lưu trữ bằng thiết bị số"))
for x in [
    "<b>Dung lượng khổng lồ, kích thước nhỏ gọn:</b> một thẻ nhớ 256 GB (bằng một móng tay) chứa được hàng trăm nghìn cuốn sách; các dịch vụ đám mây có sức chứa gần như không giới hạn.",
    "<b>Truy xuất cực nhanh:</b> tìm một từ trong hàng triệu trang chỉ trong tích tắc nhờ bộ nhớ và công cụ tìm kiếm.",
    "<b>Sao chép không suy giảm chất lượng:</b> bản sao kĩ thuật số giống hệt bản gốc, có thể nhân bản vô số lần, không bị ố vàng, rách nát như giấy.",
    "<b>Dễ sửa đổi, dễ sắp xếp:</b> có thể chèn, xoá, đổi tên, phân loại, nén, mã hoá và khôi phục dữ liệu.",
    "<b>Dễ chia sẻ và truyền đi xa:</b> gửi qua mạng tới bất kì đâu trong vài giây với chi phí rất thấp.",
    "<b>Dễ sao lưu, bền vững:</b> lưu nhiều bản ở nhiều nơi (ổ cứng, USB, đám mây) để phòng mất mát.",
    "<b>Tiết kiệm:</b> giảm chi phí in ấn, kho bãi, vận chuyển và nhân công.",
]:
    story.append(B(x))
story.append(H4("d) Đơn vị lưu trữ thông tin và cách chuyển đổi"))
story.append(TB([
    ["Thứ tự", "Đơn vị", "Kí hiệu", "Giá trị"],
    ["1", "bit (bit nhị phân)", "bit", "0 hoặc 1 – đơn vị nhỏ nhất"],
    ["2", "Byte", "B", "1 B = 8 bit"],
    ["3", "Kilobyte", "KB", "1 KB = 2¹⁰ B = 1 024 B"],
    ["4", "Megabyte", "MB", "1 MB = 2¹⁰ KB = 1 024 KB = 2²⁰ B"],
    ["5", "Gigabyte", "GB", "1 GB = 2¹⁰ MB = 1 024 MB = 2³⁰ B"],
    ["6", "Terabyte", "TB", "1 TB = 2¹⁰ GB = 1 024 GB = 2⁴⁰ B"],
    ["7", "Petabyte", "PB", "1 PB = 2¹⁰ TB = 1 024 TB = 2⁵⁰ B"],
], [42, 100, 58, 265], font="cell"))
story.append(BOX([
    P("<b>Quy tắc vàng:</b> kể từ Byte, mỗi đơn vị hơn kém nhau <b>2¹⁰ = 1 024 lần</b> (không phải 1 000). "
      "Muốn đổi từ đơn vị <b>lớn sang nhỏ</b> → <b>nhân</b> 1 024; từ đơn vị <b>nhỏ sang lớn</b> → <b>chia</b> 1 024. "
      "Bước nhảy cách n bậc thì nhân/chia với 1 024ⁿ.", "note"),
    P("<b>Ví dụ 1:</b> 3 MB = 3 × 1 024 = 3 072 KB.   <b>Ví dụ 2:</b> 2 GB = 2 × 1 024 × 1 024 = 2 097 152 KB.   "
      "<b>Ví dụ 3:</b> 2 048 B = 2 048 : 1 024 = 2 KB.   <b>Ví dụ 4:</b> 3 MB = 3 × 1 024 × 1 024 × 8 = 25 165 824 bit.", "note"),
], bg=BGAMB, border=AMBER, leftbar=AMBER))
story.append(BOX([P("<b>Ghi nhớ nhanh A1:</b> Thông tin = hiểu biết; dữ liệu = thông tin đã vào máy. "
                    "Máy tính xử lí thông tin theo 3 bước: <b>vào → xử lí → ra</b> (kèm lưu trữ & truyền). "
                    "1 B = 8 bit; 1 KB = 1 024 B; cứ lên một bậc thì ×1 024. "
                    "Lưu trữ số hơn hẳn lưu trữ giấy ở 7 điểm: nhiều – nhanh – không hỏng – dễ sửa – dễ gửi – dễ sao lưu – rẻ.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))

story.append(H3("II.1.2. Vai trò của máy tính và thiết bị thông minh trong nền kinh tế tri thức"))
story.append(BOX([P("<b>Yêu cầu cần đạt:</b> Trình bày được những đóng góp cơ bản của tin học đối với xã hội; "
                    "nhận biết thiết bị số thông dụng ngoài máy tính để bàn và laptop; giới thiệu thành tựu nổi bật ở một số mốc thời gian. "
                    "Nêu ví dụ về thiết bị thông minh; giải thích vai trò của chúng với xã hội và CMCN 4.0; "
                    "giải thích được chúng cũng là hệ thống xử lí thông tin; nêu ví dụ đóng góp của tin học.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(H4("a) Thiết bị thông minh là gì?"))
story.append(P("<b>Thiết bị thông minh</b> là thiết bị điện tử có thể hoạt động <b>tự chủ ở một mức độ nhất định</b> "
               "nhờ phần mềm điều khiển được cài sẵn, đồng thời có khả năng <b>kết nối, tương tác với thiết bị khác qua mạng "
               "không dây</b> (wifi, bluetooth, 3G/4G/5G, hồng ngoại, RFID) để tiếp nhận – xử lí – truyền dữ liệu. "
               "Nhiều thiết bị còn được tích hợp <b>AI</b> để «bắt chước» một số hành vi, tư duy của con người."))
story.append(TB([
    ["Nhóm", "Thiết bị tiêu biểu", "Dấu hiệu nhận biết"],
    ["Thiết bị cá nhân", "Điện thoại thông minh, máy tính bảng, laptop, đồng hồ thông minh, kính thông minh", "Có hệ điều hành, cài được ứng dụng, kết nối Internet"],
    ["Thiết bị trong nhà", "Tivi thông minh, loa thông minh, robot hút bụi, tủ lạnh/máy giặt thông minh, camera an ninh IP, công tơ điện tử", "Có cảm biến, tự động điều chỉnh, điều khiển từ xa bằng giọng nói/điện thoại"],
    ["Thiết bị công cộng", "Camera giao thông thông minh, thẻ RFID thu phí không dừng, xe tự hành, máy ATM, rô-bốt công nghiệp, cảm biến nông nghiệp", "Thu thập dữ liệu tự động, gửi về trung tâm, nhận lệnh điều khiển"],
], [85, 245, 135], font="cell"))
story.append(P("<b>Phân biệt:</b> đồng hồ lịch vạn niên, cân điện tử cơ học, máy ảnh số đời cũ, ổ cắm điện thông thường "
               "không phải thiết bị thông minh vì không có khả năng kết nối mạng và xử lí tự chủ; "
               "đồng hồ kết nối bluetooth với điện thoại thì <b>là</b> thiết bị thông minh."))
story.append(H4("b) Thiết bị thông minh chính là một hệ thống xử lí thông tin"))
story.append(P("Mọi thiết bị thông minh đều có đủ 4 thành phần của một hệ thống xử lí thông tin:"))
story.append(TB([
    ["Thành phần", "Vai trò", "Ví dụ trên điện thoại thông minh"],
    ["Đầu vào", "Nhận tín hiệu, thu thập dữ liệu", "Cảm biến vân tay, camera, micro, GPS, màn hình cảm ứng"],
    ["Xử lí & điều khiển", "Phân tích, ra quyết định theo chương trình", "Chip xử lí, hệ điều hành Android/iOS, ứng dụng AI"],
    ["Bộ nhớ / lưu trữ", "Giữ dữ liệu và chương trình", "RAM, bộ nhớ trong, thẻ nhớ, dữ liệu trên đám mây"],
    ["Đầu ra & truyền thông", "Trả kết quả, điều khiển, gửi dữ liệu đi", "Màn hình, loa, rung, wifi/4G gửi ảnh lên mạng"],
], [92, 175, 198], font="cell"))
story.append(H4("c) Đóng góp cơ bản của tin học đối với xã hội"))
story.append(TB([
    ["Lĩnh vực", "Đóng góp", "Ví dụ cụ thể"],
    ["Quản lí", "Xử lí nghiệp vụ nhanh, chính xác, tiết kiệm", "Quản lí học sinh, tài khoản ngân hàng, bán hàng, đặt vé máy bay"],
    ["Tự động hoá", "Thay con người làm việc lặp lại, nguy hiểm", "Rô-bốt hàn trong nhà máy, camera giám sát giao thông 24/7, tưới tiêu tự động"],
    ["Khoa học – kĩ thuật", "Tính toán, mô phỏng, dự báo", "Dự báo thời tiết, giải mã gen, thiết kế cầu đường, mô phỏng dịch bệnh"],
    ["Giáo dục", "Học mọi lúc mọi nơi, nguồn học liệu mở", "Lớp học trực tuyến Zoom/Google Meet, bài giảng điện tử, từ điển trực tuyến"],
    ["Y tế", "Quản lí hồ sơ, khám chữa bệnh từ xa", "Bệnh án điện tử, telemedicine, đặt lịch khám trực tuyến"],
    ["Kinh tế – thương mại", "Thương mại điện tử, thanh toán không dùng tiền mặt", "Mua hàng online, mobile banking, ví điện tử"],
    ["Giao tiếp cộng đồng", "Kết nối, chia sẻ thông tin tức thời", "Thư điện tử, mạng xã hội, diễn đàn, nhóm chat"],
    ["Giải trí", "Nội dung số phong phú", "Nghe nhạc, xem phim, trò chơi trực tuyến, mạng xã hội"],
], [88, 180, 197], font="cell"))
story.append(H4("d) Các mốc thành tựu nổi bật của ngành tin học"))
story.append(TB([
    ["Năm / giai đoạn", "Thành tựu", "Ý nghĩa"],
    ["1946", "Máy tính điện tử ENIAC ra đời", "Mở đầu kỉ nguyên máy tính điện tử"],
    ["1957", "Ngôn ngữ lập trình bậc cao FORTRAN", "Lập trình viên mô tả thuật toán thay vì viết mã máy; sau này có C, Pascal, Java, Python"],
    ["1964", "Hệ điều hành OS/360 trên dòng máy IBM/360", "Đặt nền móng cho các hệ điều hành hiện đại (Windows, macOS, Linux, Android, iOS)"],
    ["1969 – 1983", "ARPANET (1969) và bộ giao thức TCP/IP (1983)", "Nền tảng kĩ thuật của Internet"],
    ["1971", "Bộ vi xử lí Intel 4004", "Máy tính trở nên nhỏ gọn, rẻ, dẫn đến máy tính cá nhân"],
    ["1981", "Máy tính cá nhân IBM PC", "Đưa máy tính vào văn phòng và gia đình"],
    ["1989 – 1992", "World Wide Web (Tim Berners-Lee)", "Web bùng nổ; Internet trở thành nguồn thông tin toàn cầu"],
    ["Thập niên 1990", "Hệ quản trị cơ sở dữ liệu, thư điện tử, thương mại điện tử", "Tách dữ liệu khỏi chương trình; kinh doanh trực tuyến phát triển"],
    ["2007", "Điện thoại thông minh thế hệ mới", "Internet di động, cảm biến và ứng dụng đi cùng con người mọi lúc"],
    ["Thập niên 2010 đến nay", "Điện toán đám mây, Big Data, IoT, AI, CMCN 4.0", "Sản xuất thông minh, nền kinh tế tri thức; siêu máy tính Fugaku (2020) đạt trên 400 petaflops"],
], [78, 190, 197], font="cellsm"))
story.append(H4("e) Cách mạng công nghiệp 4.0 và kinh tế tri thức"))
story.append(TB([
    ["Cuộc cách mạng", "Thời kì", "Công nghệ tiêu biểu"],
    ["1.0", "Cuối TK XVIII", "Động cơ hơi nước, cơ khí hoá"],
    ["2.0", "Cuối TK XIX – đầu TK XX", "Điện năng, sản xuất hàng loạt"],
    ["3.0", "Giữa TK XX (thập niên 1960–1970)", "Máy tính điện tử, tự động hoá, điện tử hoá"],
    ["4.0", "Đầu TK XXI đến nay", "AI, IoT, điện toán đám mây, dữ liệu lớn, công nghệ sinh học, vật liệu mới"],
], [70, 135, 260], font="cell"))
story.append(P("Cách mạng công nghiệp 4.0 dựa trên nền tảng <b>công nghệ số</b>, làm mờ ranh giới giữa thế giới thực và thế giới ảo, "
               "tạo ra <b>sản xuất thông minh</b>. <b>Nền kinh tế tri thức</b> lấy tri thức làm động lực tăng trưởng chính; "
               "thiết bị thông minh là thành phần chủ chốt của các hệ thống IoT. Ví dụ: camera thông minh nhận diện biển số xe "
               "→ gửi dữ liệu về trung tâm → AI phân tích và tự động phạt nguội, không cần người trực tiếp ghi chép."))
story.append(BOX([P("<b>Ghi nhớ nhanh A2:</b> Thiết bị thông minh = <b>tự chủ + kết nối + xử lí dữ liệu</b>. "
                    "Nó là một hệ thống xử lí thông tin (vào – xử lí – nhớ – ra). "
                    "Tin học đóng góp 5 nhóm lớn: quản lí, tự động hoá, khoa học – kĩ thuật, thay đổi cách làm việc, giao tiếp cộng đồng. "
                    "Nhớ 4 mốc: <b>1957 FORTRAN – 1964 OS/360 – 1983 TCP/IP – 1992 WWW</b>. "
                    "CMCN 3.0 gắn với máy tính; CMCN 4.0 gắn với AI – IoT – Cloud – Big Data.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))

story.append(H3("II.1.3. Kĩ năng sử dụng thiết bị số của mỗi công dân"))
story.append(BOX([P("<b>Yêu cầu cần đạt:</b> Khởi động được một số thiết bị số thông dụng; "
                    "sử dụng được các tệp dữ liệu, các chức năng và phần mềm ứng dụng cơ bản cài sẵn trên các thiết bị đó.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(TB([
    ["Kĩ năng", "Các thao tác cốt lõi", "Lưu ý / lỗi hay gặp"],
    ["Khởi động, tắt máy", "Nhấn nút nguồn → chờ hệ điều hành nạp → đăng nhập (mật khẩu / vân tay / khuôn mặt). Tắt máy bằng lệnh Shut down, không rút điện đột ngột.", "Không tắt máy khi đang cập nhật; nếu máy treo, nhấn giữ nút nguồn 5–10 giây."],
    ["Quản lí tệp và thư mục", "Tạo thư mục, tạo tệp, đổi tên, sao chép – dán, di chuyển, xoá, nén/giải nén, tìm kiếm theo tên/ngày/loại.", "Đặt tên tệp dễ nhớ, có phần mở rộng đúng (.docx, .xlsx, .jpg, .mp3, .pdf); không lưu mọi thứ trên Desktop."],
    ["Phần mềm ứng dụng cơ bản", "Trình duyệt web; soạn thảo văn bản; bảng tính; trình chiếu; email; xem ảnh/video; nghe nhạc; ghi chú; lịch; bản đồ; máy tính; trình quét virus.", "Chỉ cài ứng dụng từ kho chính thức; đọc kĩ quyền truy cập trước khi bấm «Đồng ý»."],
    ["Kết nối", "Bật/tắt wifi, bluetooth, dữ liệu di động; chia sẻ tệp; in ấn; chiếu màn hình.", "Tắt wifi/bluetooth khi không dùng; tránh dùng wifi công cộng cho giao dịch ngân hàng."],
    ["Bảo trì & an toàn", "Cập nhật hệ điều hành và ứng dụng; sao lưu dữ liệu; quét virus; sắp xếp bộ nhớ; sạc pin đúng cách.", "Sao lưu theo quy tắc 3-2-1: 3 bản, 2 loại thiết bị, 1 bản ở ngoài (đám mây)."],
], [88, 249, 128], font="cellsm"))
story.append(P("<b>Quy trình mẫu (thực hành):</b> (1) Khởi động laptop, đăng nhập → (2) Mở trình duyệt, tải tệp «tailieu.pdf» "
               "từ trang học liệu mở → (3) Tạo thư mục «Tin_hoc_10» trong Documents → (4) Sao chép tệp vào thư mục, đổi tên "
               "thành «Bai1_Thong_tin.pdf» → (5) Mở tệp bằng trình đọc PDF và ghi chú nội dung chính → (6) Sao lưu lên "
               "Google Drive → (7) Quét virus nhanh bằng Windows Defender → (8) Đăng xuất và tắt máy đúng cách."))
story.append(BOX([P("<b>Ghi nhớ nhanh A3:</b> «Khởi động → Đăng nhập → Tệp → Ứng dụng → Kết nối → Sao lưu → Tắt máy». "
                    "Kĩ năng quan trọng nhất là quản lí tệp và giữ an toàn dữ liệu; mọi thao tác đều có thể học bằng cách làm thật trên thiết bị.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(PageBreak())

# ---- II.2 CHU DE B -------------------------------------------------------
story.append(H2("II.2. Chủ đề B. Mạng máy tính và Internet"))
story.append(H3("II.2.1. Khái niệm mạng máy tính, Internet, IoT; phân loại mạng máy tính"))
story.append(BOX([P("<b>Yêu cầu cần đạt:</b> Nêu được một số dịch vụ cụ thể mà Điện toán đám mây cung cấp cho người dùng; "
                    "nêu được khái niệm Internet vạn vật (IoT). Trình bày được những thay đổi về chất lượng cuộc sống, "
                    "phương thức học tập và làm việc khi mạng máy tính phổ biến; so sánh được mạng LAN và Internet; "
                    "nêu ví dụ cụ thể về thay đổi do IoT đem lại và phát biểu ý kiến cá nhân về lợi ích của IoT.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(H4("a) Mạng máy tính và các thành phần"))
story.append(P("<b>Mạng máy tính</b> là tập hợp các máy tính và thiết bị được kết nối với nhau theo một cách thức nhất định "
               "thông qua đường truyền và giao thức chung, nhằm <b>chia sẻ tài nguyên và trao đổi dữ liệu</b>."))
story.append(TB([
    ["Thành phần", "Vai trò", "Thiết bị / ví dụ"],
    ["Thiết bị đầu cuối", "Nơi phát sinh, nhận và xử lí dữ liệu", "Máy tính để bàn, laptop, điện thoại, máy in, máy chủ (server), camera IP"],
    ["Thiết bị kết nối mạng", "Chuyển tiếp, định tuyến dữ liệu", "Hub (bộ chia), Switch (bộ chuyển mạch), Router (bộ định tuyến), Access Point (điểm phát wifi), modem"],
    ["Đường truyền", "Môi trường truyền tín hiệu", "Cáp mạng (UTP), cáp quang, sóng wifi, 3G/4G/5G, bluetooth, vệ tinh"],
    ["Giao thức", "Bộ quy tắc để các máy «hiểu» nhau", "TCP/IP, HTTP/HTTPS, FTP, SMTP, Wi-Fi (IEEE 802.11)"],
    ["Phần mềm, dịch vụ", "Cung cấp tiện ích cho người dùng", "Trình duyệt web, thư điện tử, dịch vụ đám mây, ứng dụng mạng xã hội"],
], [100, 165, 200], font="cell"))
story.append(H4("b) Phân loại mạng máy tính"))
story.append(TB([
    ["Tiêu chí", "Các loại", "Đặc điểm"],
    ["Theo phạm vi địa lí", "LAN – MAN – WAN", "LAN (Local Area Network): phạm vi nhỏ (nhà, trường, cơ quan). MAN: quy mô thành phố. WAN (Wide Area Network): phạm vi rộng, liên kết nhiều LAN. Internet là WAN lớn nhất, quy mô toàn cầu."],
    ["Theo phương thức truyền", "Mạng có dây – mạng không dây", "Cáp mạng/cáp quang cho tốc độ cao, ổn định; wifi/4G/5G/bluetooth cho tính cơ động."],
    ["Theo cách tổ chức", "Client – Server và ngang hàng (P2P)", "Client–Server: máy khách gửi yêu cầu, máy chủ đáp ứng. P2P: các máy vừa là khách vừa là chủ."],
    ["Theo mục đích sử dụng", "Mạng cá nhân, mạng doanh nghiệp, mạng công cộng", "PAN (cá nhân, vài mét), Intranet (nội bộ cơ quan), Extranet, Internet (công cộng)."],
], [92, 113, 260], font="cellsm"))
story.append(H4("c) So sánh mạng LAN và Internet (dạng bài rất hay gặp)"))
story.append(TB([
    ["Tiêu chí", "Mạng LAN", "Internet"],
    ["Phạm vi, quy mô", "Nhỏ: một phòng, một nhà, một trường học, một cơ quan", "Toàn cầu: mạng của các mạng máy tính trên khắp thế giới"],
    ["Phương thức kết nối", "Các máy nối trực tiếp qua Switch/Hub/wifi nội bộ, dùng đường truyền riêng", "Các LAN được nối với nhau qua Router và đường truyền của nhà cung cấp dịch vụ Internet (ISP: Viettel, VNPT, FPT…)"],
    ["Chủ sở hữu, quản lí", "Thuộc sở hữu của một cá nhân/tổ chức; do tổ chức đó quản lí, đặt quy tắc", "Không thuộc sở hữu của riêng ai; chỉ có các tổ chức điều phối tài nguyên (tên miền, địa chỉ IP) và tiêu chuẩn hoá"],
    ["Tốc độ, độ trễ", "Thường cao và ổn định trong nội bộ", "Phụ thuộc đường truyền và nhà mạng"],
    ["Dịch vụ", "Chia sẻ tệp, máy in, phần mềm nội bộ", "Web, email, mạng xã hội, đám mây, thương mại điện tử, học trực tuyến…"],
    ["Mức độ rủi ro", "Thấp hơn, dễ kiểm soát", "Cao hơn: tin giả, mã độc, lừa đảo, lộ dữ liệu"],
], [92, 188, 185], font="cellsm"))
story.append(P("<b>Lưu ý:</b> trên Router có cổng LAN (nối thiết bị nội bộ) và cổng WAN/INTERNET (nối ra nhà mạng). "
               "Nếu địa chỉ đích không nằm trong LAN, Router sẽ chuyển gói dữ liệu ra cổng Internet."))
story.append(H4("d) Điện toán đám mây và các dịch vụ cụ thể"))
story.append(P("<b>Điện toán đám mây (Cloud Computing)</b> là mô hình phân phối tài nguyên công nghệ thông tin "
               "(máy chủ, lưu trữ, cơ sở dữ liệu, mạng, phần mềm…) theo nhu cầu qua Internet, thanh toán theo mức sử dụng "
               "(miễn phí hoặc trả phí). Người dùng đăng kí thuê bao, được cấp tài khoản và truy cập tài nguyên «đâu đó trên mạng»."))
story.append(TB([
    ["Dịch vụ", "Tên đầy đủ", "Cung cấp cái gì?", "Ví dụ cụ thể"],
    ["SaaS", "Software as a Service – Phần mềm như là dịch vụ", "Cho thuê quyền sử dụng phần mềm ứng dụng; không cần cài đặt, không phải quản lí máy chủ", "Gmail, Google Docs, Microsoft 365, Zoom, Google Translate"],
    ["PaaS", "Platform as a Service – Nền tảng như là dịch vụ", "Cho thuê môi trường/nền tảng để lập trình viên xây dựng, chạy và quản lí ứng dụng", "Google App Engine, Microsoft Azure App Service, nền tảng quản trị CSDL thuê ngoài"],
    ["IaaS", "Infrastructure as a Service – Hạ tầng như là dịch vụ", "Cho thuê hạ tầng phần cứng: máy chủ ảo, thiết bị lưu trữ, mạng", "Google Drive, Dropbox, OneDrive (lưu trữ); máy chủ ảo Amazon EC2, Azure VM"],
], [45, 120, 170, 130], font="cellsm"))
story.append(B("Các dịch vụ cụ thể khác: <b>lưu trữ và đồng bộ dữ liệu</b> (Drive, Dropbox), <b>thư điện tử</b> (Gmail), "
               "<b>họp trực tuyến</b> (Zoom, Meet), <b>soạn thảo trực tuyến</b> (Google Docs), <b>nghe nhạc/xem phim trực tuyến</b>, "
               "<b>sao lưu ảnh tự động</b>, <b>chạy máy chủ ảo</b>.", "bullet"))
story.append(P("<b>Lợi ích:</b> dùng mọi lúc mọi nơi, không phụ thuộc thiết bị cá nhân (tính mềm dẻo, sẵn sàng cao); "
               "chất lượng cao nhờ nhà cung cấp chuyên nghiệp; chi phí thấp vì chia sẻ tài nguyên và chỉ trả theo mức dùng. "
               "<b>Lưu ý:</b> đọc báo điện tử không phải dùng dịch vụ đám mây (đó là truy cập thông tin công cộng); "
               "dùng Gmail, Google Drive, Zoom thì là dùng dịch vụ đám mây."))
story.append(H4("e) Internet vạn vật (IoT)"))
story.append(P("<b>IoT (Internet of Things – Internet vạn vật)</b> là việc liên kết các thiết bị thông minh "
               "(được gắn cảm biến, cài phần mềm chuyên dụng) qua mạng để <b>tự động thu thập, trao đổi và xử lí dữ liệu</b> "
               "phục vụ các mục đích khác nhau, không nhất thiết có sự tương tác trực tiếp giữa người với người hay người với máy tính. "
               "Các thiết bị có thể kết nối qua Internet, LAN, bluetooth, RFID hoặc mạng cảm biến."))
story.append(TB([
    ["Ứng dụng IoT", "Cách hoạt động ngắn gọn", "Lợi ích"],
    ["Thu phí không dừng", "Thẻ RFID trên kính ô tô → thiết bị đọc thẻ → truyền dữ liệu về trung tâm → trừ tiền, mở barie", "Không phải dừng xe, giảm ùn tắc, minh bạch"],
    ["Nhà thông minh", "Cảm biến nhiệt độ/ánh sáng → bộ điều khiển → tự bật điều hoà, đèn, rèm; điều khiển bằng giọng nói", "Tiện nghi, tiết kiệm điện, an toàn (báo cháy, báo trộm)"],
    ["Công tơ điện tử", "Đo điện năng liên tục → gửi số liệu về công ty điện qua mạng", "Không cần nhân công ghi chỉ số, số liệu chính xác, phát hiện bất thường"],
    ["Camera giao thông thông minh", "Camera + AI nhận dạng biển số → gửi về trung tâm → phát hiện vi phạm, phạt nguội", "Giảm tải cho cảnh sát, minh bạch, xử lí 24/24"],
    ["Nông nghiệp thông minh", "Cảm biến độ ẩm đất, nhiệt độ → tự động tưới, bón phân", "Tiết kiệm nước, tăng năng suất"],
    ["Đồng hồ sức khoẻ / y tế từ xa", "Cảm biến nhịp tim, SpO₂ → gửi về điện thoại/bác sĩ", "Theo dõi sức khoẻ, cảnh báo sớm"],
], [100, 240, 125], font="cellsm"))
story.append(P("<b>Ý kiến cá nhân mẫu về lợi ích của IoT:</b> «Theo em, IoT giúp con người có được dữ liệu đúng lúc, "
               "tự động và liên tục, nhờ đó quyết định nhanh và chính xác hơn. Ví dụ hệ thống camera giao thông giúp phát hiện "
               "vi phạm 24/24 mà không cần người đứng đường. Tuy nhiên, IoT cũng đặt ra vấn đề bảo mật và quyền riêng tư, "
               "vì vậy cần mã hoá dữ liệu, đặt mật khẩu mạnh cho thiết bị và chỉ chia sẻ dữ liệu cần thiết.»"))
story.append(H4("f) Thay đổi chất lượng cuộc sống, học tập và làm việc"))
for x in [
    "<b>Giao tiếp:</b> liên lạc tức thời qua email, mạng xã hội, gọi video; chia sẻ kiến thức và phản hồi ngay lập tức ở bất cứ đâu.",
    "<b>Học tập:</b> Internet là nguồn thông tin khổng lồ; nền tảng học trực tuyến, bài giảng điện tử, thư viện số giúp học mọi lúc, học suốt đời.",
    "<b>Làm việc:</b> họp trực tuyến, làm việc từ xa, cộng tác trên tài liệu đám mây, giao dịch và thủ tục hành chính trực tuyến.",
    "<b>Đời sống:</b> mua sắm, thanh toán, đặt vé, xem phim, nghe nhạc, khám bệnh từ xa, giải trí và thể thao thông minh.",
    "<b>Mặt trái:</b> tin giả, lừa đảo, nghiện mạng, lộ thông tin cá nhân, khoảng cách số – vì vậy cần kĩ năng tự bảo vệ.",
]:
    story.append(B(x))
story.append(BOX([P("<b>Ghi nhớ nhanh B1:</b> LAN = nhỏ, có chủ; Internet = toàn cầu, không ai sở hữu. "
                    "Đám mây có <b>3 dịch vụ: SaaS (phần mềm) – PaaS (nền tảng) – IaaS (hạ tầng)</b>; "
                    "nhớ ví dụ: Gmail/Zoom (SaaS), Google Drive/Dropbox (IaaS), nền tảng lập trình (PaaS). "
                    "IoT = <b>cảm biến + mạng + xử lí tự động</b>; nhớ 4 ví dụ: thu phí không dừng, nhà thông minh, công tơ điện tử, camera giao thông.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))

story.append(H3("II.2.2. Sử dụng dịch vụ web và tự bảo vệ khi tham gia mạng"))
story.append(BOX([P("<b>Yêu cầu cần đạt:</b> Trình bày sơ lược về phần mềm độc hại; nêu một vài cách phòng vệ khi bị bắt nạt "
                    "trên mạng; nêu nguy cơ, tác hại khi tham gia Internet bất cẩn. Trình bày cách đề phòng tác hại. "
                    "Vận dụng: dùng công cụ ngăn ngừa, loại bỏ phần mềm độc hại; dùng chức năng xử lí thông tin (dịch tự động "
                    "văn bản, tiếng nói); khai thác học liệu mở; tự bảo vệ dữ liệu cá nhân.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(H4("a) Dịch vụ web và công cụ xử lí thông tin thông dụng"))
story.append(TB([
    ["Dịch vụ / công cụ", "Chức năng chính", "Quy trình sử dụng ngắn gọn"],
    ["Máy tìm kiếm (Google, Bing)", "Tìm trang web, hình ảnh, video theo từ khoá", "Gõ từ khoá → đọc kết quả → kiểm tra nguồn → mở trang tin cậy → lưu trích dẫn"],
    ["Dịch tự động văn bản (Google Translate, DeepL)", "Dịch văn bản từ tiếng này sang tiếng khác", "Mở trang dịch → chọn ngôn ngữ nguồn/đích → nhập hoặc dán văn bản → đọc bản dịch → rà soát lại"],
    ["Nhận dạng tiếng nói / đọc văn bản", "Biến giọng nói thành chữ và ngược lại", "Bật micro → nói rõ → kiểm tra văn bản được tạo → sửa lỗi → sao chép/gửi"],
    ["Học liệu mở (OER)", "Tài nguyên giáo dục miễn phí, cho phép dùng, sửa, chia sẻ hợp pháp", "Tìm nguồn có giấy phép mở (Creative Commons, Khan Academy, MIT OCW, thư viện số, bài giảng điện tử) → đọc điều kiện sử dụng → tải về → ghi rõ nguồn tác giả khi dùng lại"],
    ["Thư điện tử, mạng xã hội, diễn đàn", "Trao đổi thông tin, hợp tác, học nhóm", "Soạn nội dung rõ ràng → kiểm tra người nhận → đính kèm tệp → gửi; không tiết lộ thông tin nhạy cảm"],
], [115, 165, 185], font="cellsm"))
story.append(H4("b) Nguy cơ và tác hại khi tham gia Internet thiếu hiểu biết"))
story.append(TB([
    ["Nguy cơ", "Biểu hiện", "Tác hại"],
    ["Tin giả, tin phản văn hoá", "Tin bịa đặt, giật gân, nội dung bạo lực, lệch chuẩn", "Nhận thức sai lệch, hoang mang, kích động hành vi xấu; người đăng lại có thể bị xử phạt"],
    ["Lừa đảo trên mạng", "Lập trang giả mạo người quen, hứa «việc nhẹ lương cao», dụ nạp thẻ, đầu tư tiền ảo lãi cao", "Mất tiền, mất tài khoản, bị đánh cắp danh tính"],
    ["Lộ thông tin cá nhân", "Đăng ảnh CCCD, số điện thoại, địa chỉ, tài khoản ngân hàng, OTP", "Bị mạo danh, bị tống tiền, mất tiền, bị quấy rối"],
    ["Bắt nạt trên mạng", "Xỉ vả, lăng nhục, đe doạ tung ảnh, vu khống, tẩy chay", "Tổn thương tâm lí, trầm cảm, tự cô lập; có thể bị xử lí pháp lí"],
    ["Nghiện mạng, nghiện game", "Dành quá nhiều thời gian trực tuyến", "Suy giảm sức khoẻ, kết quả học tập, rối loạn giấc ngủ"],
    ["Phần mềm độc hại", "Tải phần mềm bẻ khoá, mở link lạ, cắm USB không rõ nguồn", "Mất dữ liệu, máy bị chiếm quyền, bị mã hoá tống tiền"],
], [95, 185, 185], font="cellsm"))
story.append(H4("c) Phần mềm độc hại (malware) – phân loại và phòng chống"))
story.append(P("<b>Phần mềm độc hại (malware)</b> là phần mềm được viết ra với ý đồ xấu, gây hại cho người dùng, "
               "thiết bị hoặc dữ liệu. Ba nhóm chính: <b>virus, worm, trojan</b>."))
story.append(TB([
    ["Loại", "Tính hoàn chỉnh", "Cơ chế lây nhiễm", "Tác hại"],
    ["Virus", "Không phải phần mềm hoàn chỉnh: chỉ là đoạn mã độc, phải gắn vào chương trình khác", "Khi chạy chương trình bị nhiễm, virus chèn bản sao vào các chương trình khác; lây qua trao đổi tệp/USB", "Gây nhiễu loạn hoạt động, hỏng phần mềm, xoá dữ liệu; không tự lan sang máy khác nếu không trao đổi dữ liệu"],
    ["Worm (sâu)", "Là một chương trình hoàn chỉnh", "Tự phát tán qua mạng: lợi dụng lỗ hổng hệ điều hành hoặc lừa người dùng mở liên kết/đính kèm email", "Lây lan rất nhanh, phá hoại dữ liệu, tê liệt hệ thống; ví dụ Melissa (1999), Code Red (2001), WannaCry (2017)"],
    ["Trojan (ngựa thành Troa)", "Không có đặc trưng về tính hoàn chỉnh, ít chú trọng lây lan", "Cài đặt trực tiếp hoặc dùng cơ chế giống worm, thường ngụy trang thành phần mềm hữu ích", "Ăn cắp thông tin, chiếm quyền điều khiển máy; các dạng: spyware, keylogger, backdoor, rootkit"],
], [70, 105, 155, 135], font="cellsm"))
story.append(B("Một số mã độc khác: <b>ransomware</b> (mã hoá dữ liệu đòi tiền chuộc), <b>spyware</b> (gián điệp), "
               "<b>keylogger</b> (ghi bàn phím), <b>backdoor</b> (cửa sau truy cập ngầm), <b>rootkit</b> (chiếm quyền cao nhất), "
               "<b>adware</b> (quảng cáo), <b>phishing</b> (trang web lừa đảo).", "bullet"))
story.append(P("<b>Phòng chống:</b> không tải phần mềm bẻ khoá/nguồn lạ; không mở liên kết, tệp đính kèm khi chưa xác minh "
               "(gọi điện hỏi lại người gửi); cập nhật hệ điều hành và phần mềm; dùng mật khẩu mạnh, bật xác thực 2 yếu tố; "
               "cài và cập nhật phần mềm diệt virus; sao lưu dữ liệu định kì; quét USB, thẻ nhớ trước khi mở."))
story.append(TB([
    ["Công cụ", "Cách dùng", "Các chế độ quét / lưu ý"],
    ["Windows Defender (Windows Security)", "Start → Settings → Windows Security → Virus & threat protection → Scan options → chọn kiểu quét → Scan now", "Quick scan (quét nhanh vùng nguy cơ cao); Full scan (quét toàn bộ ổ đĩa); Custom scan (quét thư mục tự chọn); Windows Defender Offline scan (mã độc khó gỡ)"],
    ["Phần mềm diệt virus khác", "Cài đặt → cập nhật mẫu virus → quét định kì", "Kaspersky, Avast, AVG, McAfee, Norton, Panda, BKAV (Việt Nam); có kèm tường lửa cảnh báo web độc hại"],
    ["Chức năng quét nhanh tại chỗ", "Nháy chuột phải vào tệp/thư mục → Scan with Microsoft Defender", "Dùng ngay trước khi mở tệp vừa tải về hoặc vừa chép từ thẻ nhớ"],
], [105, 195, 165], font="cellsm"))
story.append(H4("d) Phòng vệ khi bị bắt nạt trên mạng"))
for i, x in enumerate([
    "Không kết bạn dễ dãi, không trả lời, không tranh luận với kẻ bắt nạt trên diễn đàn.",
    "Lưu giữ toàn bộ bằng chứng: chụp màn hình, lưu tin nhắn, ghi lại thời gian và tên tài khoản.",
    "Chia sẻ ngay với bố mẹ, thầy cô hoặc người thân đáng tin cậy – không im lặng chịu đựng.",
    "Dùng chức năng chặn (block), ẩn bình luận, báo cáo vi phạm với nhà quản lí nền tảng.",
    "Khi sự việc nghiêm trọng (đe doạ, tống tiền, phát tán ảnh nhạy cảm), báo cơ quan công an kèm bằng chứng.",
], 1):
    story.append(B(str(i) + ". " + x))
story.append(H4("e) Tự bảo vệ dữ liệu cá nhân"))
story.append(TB([
    ["Biện pháp", "Thực hiện cụ thể"],
    ["Mật khẩu mạnh", "Dài ít nhất 8–12 kí tự, gồm chữ hoa, chữ thường, số, kí hiệu; không dùng ngày sinh, 123456; mỗi tài khoản một mật khẩu; thay đổi định kì; không chia sẻ cho ai"],
    ["Xác thực 2 yếu tố (2FA)", "Bật thêm mã OTP/ứng dụng xác thực; không đưa mã OTP cho bất kì ai, kể cả người tự xưng nhân viên ngân hàng"],
    ["Giữ bí mật thông tin", "Không đăng công khai CCCD, địa chỉ, số điện thoại, lịch trình, tài khoản ngân hàng; cài chế độ riêng tư cho mạng xã hội"],
    ["Cẩn trọng khi đăng nhập", "Không dùng chế độ «ghi nhớ mật khẩu» trên máy công cộng; luôn đăng xuất sau khi dùng; tránh đăng nhập qua wifi công cộng không mã hoá"],
    ["Kiểm soát ứng dụng", "Chỉ cấp quyền thật sự cần thiết (camera, micro, vị trí); gỡ ứng dụng không rõ nguồn; đọc kĩ điều khoản"],
    ["Cập nhật & sao lưu", "Luôn cập nhật hệ điều hành/ứng dụng; sao lưu dữ liệu quan trọng theo quy tắc 3-2-1"],
    ["Chia sẻ có chọn lọc", "Kiểm tra nguồn tin trước khi like/share; không tiếp tay phát tán tin giả, thông tin riêng của người khác"],
], [105, 360], font="cellsm"))
story.append(BOX([P("<b>Ghi nhớ nhanh B2:</b> Malware có 3 nhóm chính: <b>virus (đoạn mã, cần vật chủ) – worm (tự lan qua mạng) – "
                    "trojan (nội gián, ăn cắp thông tin)</b>. Phòng bệnh hơn chữa bệnh: cập nhật – mật khẩu mạnh – không click link lạ – "
                    "quét virus – sao lưu. Bị bắt nạt: <b>không đáp trả → lưu bằng chứng → nói với người lớn → báo công an</b>. "
                    "Dùng web hiệu quả: tìm kiếm có kiểm chứng, dịch tự động có rà soát, học liệu mở có ghi nguồn bản quyền.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(PageBreak())

# ---- II.3 CHU DE D -------------------------------------------------------
story.append(H2("II.3. Chủ đề D. Đạo đức, pháp luật và văn hoá trong môi trường số"))
story.append(H3("II.3.1. Nghĩa vụ tuân thủ pháp lí trong môi trường số"))
story.append(BOX([P("<b>Yêu cầu cần đạt:</b> Nêu các vấn đề nảy sinh về pháp luật, đạo đức, văn hoá khi giao tiếp qua mạng "
                    "phổ biến; trình bày, giải thích nội dung cơ bản của Luật Công nghệ thông tin, Nghị định về quản lí, cung cấp, "
                    "sử dụng các sản phẩm và dịch vụ Công nghệ thông tin, Luật An ninh mạng (có ví dụ). Nêu ví dụ vi phạm bản quyền "
                    "và hậu quả; giải thích khía cạnh pháp lí của bản quyền, sở hữu, sử dụng, trao đổi thông tin số; nêu ví dụ "
                    "tác hại của chia sẻ thông tin bất cẩn và biện pháp chia sẻ an toàn, hợp pháp. Vận dụng luật để xác định "
                    "tính hợp pháp của một hành vi.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(H4("a) Những vấn đề nảy sinh khi giao tiếp qua mạng phổ biến"))
story.append(TB([
    ["Nhóm vấn đề", "Biểu hiện cụ thể"],
    ["Pháp luật", "Vi phạm bản quyền (sao chép nhạc, phim, phần mềm, bài viết); đăng tin sai sự thật, vu khống; lộ bí mật nhà nước, dữ liệu cá nhân; lừa đảo, phát tán mã độc; kinh doanh hàng cấm, đánh bạc trực tuyến"],
    ["Đạo đức", "Nói dối, mạo danh, lừa gạt; lợi dụng lòng tốt; phát tán hình ảnh riêng tư của người khác; gian lận trong học tập, thi cử trực tuyến; «ăn cắp» ý tưởng nội dung"],
    ["Văn hoá", "Ngôn từ thô tục, xúc phạm danh dự nhân phẩm; kì thị vùng miễn, giới tính; bình luận ác ý; phát tán nội dung bạo lực, đồi truỵ; thiếu tôn trọng trong giao tiếp (netiquette)"],
], [80, 385], font="cell"))
story.append(H4("b) Bản quyền thông tin và sản phẩm số"))
story.append(P("<b>Quyền tác giả</b> là quyền của tác giả đối với tác phẩm do mình sáng tạo (sáng tạo tinh thần, văn hoá). "
               "Kí hiệu <b>©</b> (Copyright) tuyên bố sản phẩm đã được bảo hộ: nghiêm cấm tổ chức, cá nhân sử dụng nếu chưa có "
               "sự đồng ý của chủ sở hữu. Luật Sở hữu trí tuệ bảo vệ cả xuất bản phẩm đã số hoá (bài viết, tranh ảnh, video) "
               "lẫn sản phẩm kĩ thuật số (trang web, phần mềm, cơ sở dữ liệu)."))
story.append(TB([
    ["Hành vi", "Đánh giá", "Căn cứ / hậu quả"],
    ["Tự ý tải bài hát, video đang «hot» rồi đăng lại lên kênh của mình để lấy view", "Vi phạm bản quyền", "Xâm phạm quyền sao chép, phân phối, truyền đạt tác phẩm (Điều 28 Luật SHTT). Bị buộc gỡ bỏ, xin lỗi, bồi thường; phạt hành chính theo Nghị định 131/2013/NĐ-CP"],
    ["Sao chép đĩa cài phần mềm có bản quyền cho bạn bè; dùng chung tài khoản khoá học trực tuyến", "Vi phạm bản quyền", "Sử dụng tác phẩm không được phép của chủ sở hữu; người mua một bản chỉ được dùng cho mình"],
    ["Trích dẫn một đoạn ngắn, ghi rõ tên tác giả và nguồn, không làm sai ý tác giả", "Không vi phạm", "Điều 25 Luật SHTT cho phép trích dẫn hợp lí tác phẩm đã công bố để bình luận, minh hoạ, viết báo, nghiên cứu, không phải trả nhuận bút"],
    ["Dùng ảnh/ nhạc có giấy phép Creative Commons, ghi nguồn đúng điều kiện", "Hợp pháp", "Tác giả đã cho phép sử dụng theo điều kiện ghi rõ (ghi nguồn, không thương mại, chia sẻ cùng giấy phép…)"],
    ["Mua bản quyền phần mềm, cài đúng số máy cho phép", "Hợp pháp", "Có sự đồng ý của chủ sở hữu thông qua hợp đồng/giấy phép"],
], [175, 65, 225], font="cellsm"))
story.append(P("<b>Hậu quả của vi phạm bản quyền:</b> bị yêu cầu gỡ bỏ sản phẩm vi phạm; bị phạt tiền "
               "(theo Nghị định 131/2013/NĐ-CP, hành vi sao chép tác phẩm trái phép có thể bị phạt 15–35 triệu đồng); "
               "phải bồi thường thiệt hại, xin lỗi công khai; uy tín cá nhân/doanh nghiệp giảm sút; "
               "trường hợp nghiêm trọng có thể bị truy cứu trách nhiệm hình sự."))
story.append(H4("c) Hệ thống văn bản pháp luật cần nhớ"))
story.append(TB([
    ["Văn bản", "Năm / số hiệu", "Nội dung cơ bản cần nhớ"],
    ["Luật Công nghệ thông tin", "2006 – số 67/2006/QH11", "Điều 12 quy định các hành vi bị cấm, trong đó khoản 2 cấm cung cấp, trao đổi, truyền đưa, lưu trữ, sử dụng thông tin số nhằm chống Nhà nước, kích động bạo lực, xuyên tạc, vu khống, xúc phạm uy tín tổ chức, danh dự nhân phẩm công dân, quảng cáo hàng hoá bất hợp pháp…"],
    ["Luật An ninh mạng", "2018 – số 24/2018/QH14 (hiệu lực 1/1/2019)", "Điều 8 khoản 1 nghiêm cấm dùng không gian mạng để chống Nhà nước, xuyên tạc lịch sử, đưa thông tin sai sự thật gây hoang mang, đăng thông tin dâm ô, đồi truỵ, xúc phạm tôn giáo, kích động bạo lực, xâm phạm quyền lợi hợp pháp của tổ chức, cá nhân"],
    ["Nghị định về quản lí, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng", "72/2013/NĐ-CP (sửa đổi bởi 27/2018/NĐ-CP)", "Quy định quản lí hoạt động Internet, trang thông tin điện tử, mạng xã hội, trò chơi trực tuyến; Điều 5 liệt kê hành vi bị cấm như lợi dụng Internet chống Nhà nước, tiết lộ bí mật nhà nước, phát tán thông tin dâm ô, giả mạo, lừa đảo, spam"],
    ["Luật Sở hữu trí tuệ", "50/2005/QH11 (sửa đổi, bổ sung 2009, 2019 – Luật 42/2019/QH14)", "Điều 25: các trường hợp dùng tác phẩm đã công bố không phải xin phép, không phải trả nhuận bút (trích dẫn hợp lí…). Điều 28: các hành vi xâm phạm quyền tác giả"],
    ["Nghị định xử phạt vi phạm hành chính về quyền tác giả, quyền liên quan", "131/2013/NĐ-CP", "Phạt tiền 5–10 triệu đồng với hành vi công bố tác phẩm trái phép; 15–35 triệu đồng với hành vi sao chép tác phẩm trái phép; buộc dỡ bỏ bản sao vi phạm"],
    ["Nghị định xử phạt VPHC lĩnh vực bưu chính, viễn thông, CNTT, giao dịch điện tử", "15/2020/NĐ-CP", "Điều 101: phạt 10–20 triệu đồng với hành vi lợi dụng mạng xã hội để cung cấp, chia sẻ thông tin giả mạo, sai sự thật, xuyên tạc; buộc gỡ bỏ thông tin"],
    ["Bộ Quy tắc ứng xử trên mạng xã hội", "Quyết định 874/QĐ-BTTTT, 17/6/2021", "Khuyến khích hành vi ứng xử văn minh: tôn trọng pháp luật, không đăng tin giả, không phát ngôn thù ghét, bảo vệ trẻ em và thông tin cá nhân"],
], [110, 105, 250], font="cellsm"))
story.append(H4("d) Chia sẻ, phổ biến thông tin bất cẩn – tác hại và biện pháp"))
story.append(P("<b>Ví dụ điển hình:</b> năm 2020, một người dùng Facebook chia sẻ lại tin «TP. Hồ Chí Minh sẽ phong toả 14 ngày» "
               "mà không kiểm chứng. Tin lan nhanh, gây hoang mang, người dân đổ xô mua hàng. Hành vi này bị nghiêm cấm theo "
               "điểm d khoản 1 Điều 8 Luật An ninh mạng và có thể bị xử phạt 10–20 triệu đồng theo khoản 1 Điều 101 "
               "Nghị định 15/2020/NĐ-CP. Ngay cả việc <b>bấm Like/Share/Comment</b> vào bài viết sai trái cũng tiếp tay lan truyền "
               "và có thể bị xem xét xử lí."))
story.append(TB([
    ["Biện pháp chia sẻ an toàn, hợp pháp", "Vì sao quan trọng?"],
    ["Kiểm tra nguồn tin, đối chiếu ít nhất 2 nguồn uy tín trước khi đăng lại", "Tránh tiếp tay phát tán tin giả, tin chưa kiểm chứng"],
    ["Tôn trọng bản quyền: chỉ đăng nội dung tự làm, có giấy phép hoặc trích dẫn hợp lí kèm tên tác giả, địa chỉ nguồn, ngày công bố", "Tránh vi phạm Luật SHTT và bị xử phạt, gỡ bỏ"],
    ["Không tuỳ tiện tiết lộ thông tin cá nhân của bản thân và của người khác", "Bảo vệ quyền riêng tư, tránh bị lợi dụng, lừa đảo"],
    ["Có hiểu biết cơ bản về quy định pháp luật về bản quyền, thông tin cá nhân, chia sẻ thông tin số", "Biết ranh giới hợp pháp – bất hợp pháp để tự bảo vệ mình"],
    ["Sử dụng biện pháp an ninh: mật khẩu mạnh, xác thực 2 yếu tố, phần mềm diệt virus, cập nhật hệ điều hành", "Ngăn chặn kẻ xấu chiếm tài khoản rồi đăng tin trái phép"],
    ["Hạn chế đăng nhập trên máy tính lạ hoặc qua mạng không đáng tin cậy; luôn đăng xuất", "Tránh lộ tài khoản, bị mạo danh"],
    ["Gỡ bỏ, cải chính ngay khi phát hiện mình chia sẻ nhầm thông tin sai; thông báo cho người bị ảnh hưởng", "Giảm thiểu hậu quả, thể hiện trách nhiệm công dân số"],
], [255, 210], font="cellsm"))
story.append(H4("e) Quy trình 4 bước xác định tính hợp pháp của một hành vi (dạng bài vận dụng cao)"))
story.append(TB([
    ["Bước", "Việc cần làm", "Câu hỏi tự đặt ra"],
    ["1", "Mô tả chính xác hành vi", "Ai làm gì, với sản phẩm/dịch vụ/information nào, trên môi trường nào, có xin phép không?"],
    ["2", "Đối chiếu với văn bản pháp luật", "Hành vi thuộc Điều 12 Luật CNTT? Điều 8 Luật An ninh mạng? Điều 5 Nghị định 72? Điều 25/28 Luật SHTT?"],
    ["3", "Kết luận tính hợp pháp", "Hợp pháp (có cho phép/thuộc trường hợp ngoại lệ) hay vi phạm (thuộc hành vi bị cấm)?"],
    ["4", "Nêu hậu quả, chế tài và cách xử lí đúng", "Phạt bao nhiêu, buộc gỡ bỏ/bồi thường những gì; cần xin phép, ghi nguồn, gỡ bài hay báo cơ quan chức năng?"],
], [38, 190, 237], font="cell"))
story.append(P("<b>Ví dụ vận dụng:</b> «Công ty A đăng bài viết và video lấy từ trang web của nhà sản xuất game nước ngoài "
               "mà không xin phép.» → Bước 1: hành vi sao chép, đăng tải tác phẩm của người khác. Bước 2: đối chiếu "
               "khoản 7, 8, 10 Điều 28 Luật Sở hữu trí tuệ (hành vi xâm phạm quyền tác giả) và Nghị định 72/2013/NĐ-CP "
               "về thông tin trên mạng. Bước 3: kết luận <b>vi phạm pháp luật</b>. Bước 4: công ty phải gỡ bài, xin phép và "
               "thoả thuận trả phí bản quyền; có thể bị xử phạt hành chính theo Nghị định 131/2013/NĐ-CP và bồi thường thiệt hại."))
story.append(BOX([P("<b>Ghi nhớ nhanh D:</b> Nhớ 4 văn bản: <b>Luật CNTT 2006 (Điều 12) – Luật An ninh mạng 2018 (Điều 8) – "
                    "Nghị định 72/2013 (Điều 5) – Luật SHTT 50/2005 (Điều 25, 28)</b>; thêm 2 nghị định xử phạt: "
                    "<b>131/2013</b> (bản quyền) và <b>15/2020, Điều 101</b> (tin giả, 10–20 triệu đồng). "
                    "© = đã được bảo hộ. Chia sẻ an toàn = <b>kiểm chứng – ghi nguồn – giữ kín thông tin – mật khẩu mạnh – không like tin sai</b>.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(PageBreak())

# ==========================================================================
# PHAN III - BANG TRA CUU NHANH
# ==========================================================================
story.append(H1("PHẦN III", "BẢNG TRA CỨU NHANH & SƠ ĐỒ GHI NHỚ"))
story.append(P("Đây là phần «bỏ túi» – nên đọc lại trong 10 phút trước khi vào phòng thi."))
story.append(H2("III.1. Bảng đổi đơn vị và công thức tính nhanh"))
story.append(TB([
    ["Đổi từ", "Sang", "Công thức", "Ví dụ"],
    ["Bit", "Byte", "Chia 8", "16 384 bit = 2 048 B = 2 KB"],
    ["B", "KB", "Chia 1 024", "3 072 B = 3 KB"],
    ["KB", "MB", "Chia 1 024", "2 048 KB = 2 MB"],
    ["MB", "KB", "Nhân 1 024", "3 MB = 3 072 KB"],
    ["GB", "KB", "Nhân 1 024²", "2 GB = 2 097 152 KB"],
    ["MB", "bit", "Nhân 1 024 × 1 024 × 8", "3 MB = 25 165 824 bit"],
], [72, 72, 160, 161], font="cell"))
story.append(P("<b>Mẹo:</b> xác định số bậc chênh lệch giữa hai đơn vị trong dãy "
               "<b>B → KB → MB → GB → TB → PB</b>, rồi dùng 1 024^mũ. Đổi ngược lại thì chia. "
               "Bài toán thực tế: một cuốn sách số hoá chiếm 50 MB; 2 000 cuốn chiếm 100 000 MB ≈ 97,66 GB → vừa với ổ 256 GB."))

story.append(H2("III.2. Các bảng so sánh «dễ nhầm»"))
story.append(H3("III.2.1. Dữ liệu – Thông tin"))
story.append(TB([
    ["Tiêu chí", "Dữ liệu", "Thông tin"],
    ["Bản chất", "Nguyên liệu thô, biểu diễn dưới dạng số, chữ, ảnh, âm thanh", "Hiểu biết/ý nghĩa thu được sau khi xử lí dữ liệu"],
    ["Vai trò", "Đầu vào của bài toán xử lí", "Kết quả đầu ra; làm thay đổi hành động của con người"],
    ["Tính phụ thuộc", "Khách quan, chưa mang nghĩa", "Phụ thuộc vào người tiếp nhận, ngữ cảnh"],
    ["Ví dụ", "37; 39; 40; 38; 41", "Nhiệt độ cơ thể 39 °C → bạn bị sốt, cần nghỉ ngơi"],
], [80, 190, 195], font="cellsm"))
story.append(H3("III.2.2. Virus – Worm – Trojan"))
story.append(TB([
    ["Tiêu chí", "Virus", "Worm", "Trojan"],
    ["Hoàn chỉnh?", "Không – chỉ là đoạn mã", "Có – chương trình hoàn chỉnh", "Không đặc trưng"],
    ["Lây qua", "Gắn vào chương trình khác, lây khi trao đổi tệp", "Tự lan qua mạng, lợi dụng lỗ hổng/lừa người dùng", "Không chú trọng lây lan; cài trực tiếp hoặc ngụy trang"],
    ["Tác hại chính", "Phá dữ liệu, nhiễu loạn máy", "Lây diện rộng, tê liệt hệ thống (WannaCry)", "Ăn cắp thông tin, chiếm quyền (spyware, keylogger, backdoor, rootkit)"],
], [72, 131, 131, 131], font="cellsm"))
story.append(H3("III.2.3. LAN – Internet và SaaS – PaaS – IaaS"))
story.append(TB([
    ["So sánh", "Bên trái", "Bên phải"],
    ["LAN ↔ Internet", "Phạm vi nhỏ; đường truyền riêng; có chủ sở hữu; dùng Switch/Hub", "Toàn cầu; nối các LAN qua Router; không ai sở hữu; qua ISP"],
    ["SaaS ↔ IaaS", "Phần mềm chạy trên mây: Gmail, Zoom, Google Docs", "Hạ tầng/thuê máy chủ, lưu trữ: Google Drive, Dropbox, máy chủ ảo"],
    ["PaaS", "Nền tảng phát triển ứng dụng: Google App Engine, Azure App Service", "Nằm giữa SaaS và IaaS"],
], [95, 185, 185], font="cellsm"))
story.append(H3("III.2.4. Bốn mức độ nhận thức trong đề"))
story.append(TB([
    ["Mức độ", "Tỉ lệ", "Động từ thường dùng", "Ví dụ"],
    ["Nhận biết", "40%", "Nêu, nhận biết, trình bày lại, liệt kê, giới thiệu", "Nêu khái niệm IoT; kể tên thiết bị thông minh"],
    ["Thông hiểu", "30%", "Phân biệt, giải thích, so sánh, minh hoạ, ví dụ", "Phân biệt dữ liệu và thông tin; so sánh LAN và Internet"],
    ["Vận dụng", "20%", "Chuyển đổi, sử dụng, khai thác, thực hiện", "Đổi 3 MB sang KB; dùng Windows Defender quét virus"],
    ["Vận dụng cao", "10%", "Vận dụng luật, phân tích tình huống, xác định tính hợp pháp, đề xuất", "Dùng Luật và Nghị định để xác định một hành vi có hợp pháp không"],
], [85, 48, 165, 167], font="cellsm"))

story.append(H2("III.3. Sơ đồ tư duy tổng hợp (dạng cây)"))
mindmap = '''GIỮA KÌ I – TIN HỌC 10
├── CHỦ ĐỀ A (40%): Máy tính và xã hội tri thức
│   ├── A1 Dữ liệu – thông tin – xử lí: thông tin ↔ dữ liệu | 3 bước vào–xử lí–ra | B, KB, MB… (×1024)
│   ├── A2 Thiết bị thông minh & tin học: tự chủ + kết nối | 5 đóng góp | 1957–1964–1983–1992 | CMCN 4.0
│   └── A3 Kĩ năng số: khởi động – tệp – ứng dụng – kết nối – sao lưu
├── CHỦ ĐỀ B (40%): Mạng máy tính và Internet
│   ├── B1: mạng → LAN/WAN → Internet | SaaS–PaaS–IaaS | IoT (cảm biến → mạng → xử lí)
│   └── B2: dịch vụ web, học liệu mở | tin giả–lừa đảo–bắt nạt | virus–worm–trojan | Defender | mật khẩu mạnh
└── CHỦ ĐỀ D (20%): Đạo đức – pháp luật – văn hoá số
    ├── Bản quyền ©, Điều 25/28 Luật SHTT
    ├── Luật CNTT (Đ12), Luật An ninh mạng (Đ8), NĐ 72/2013, NĐ 15/2020 (Đ101)
    └── Chia sẻ an toàn: kiểm chứng – ghi nguồn – bảo mật – xác định tính hợp pháp'''
story.append(BOX([Paragraph(esc(mindmap).replace("\n", "<br/>"), ParagraphStyle(
    "mind", fontName="DVM", fontSize=7.5, leading=11.2, textColor=NAVY))], bg=BG, border=LINE))

story.append(H2("III.4. Bảng thuật ngữ Anh – Việt cần nhớ"))
story.append(TB([
    ["Thuật ngữ", "Viết tắt / tiếng Anh", "Nghĩa tiếng Việt"],
    ["Bit / Byte", "bit / B", "Bit / Bai (1 B = 8 bit)"],
    ["Dữ liệu / Thông tin", "data / information", "Dữ liệu / Thông tin"],
    ["Mạng cục bộ", "LAN (Local Area Network)", "Mạng cục bộ"],
    ["Mạng diện rộng", "WAN (Wide Area Network)", "Mạng diện rộng; Internet là WAN toàn cầu"],
    ["Nhà cung cấp dịch vụ Internet", "ISP", "Viettel, VNPT, FPT…"],
    ["Điện toán đám mây", "Cloud Computing", "Cung cấp tài nguyên CNTT qua Internet theo nhu cầu"],
    ["Phần mềm / Nền tảng / Hạ tầng như dịch vụ", "SaaS / PaaS / IaaS", "Ba loại dịch vụ đám mây cơ bản"],
    ["Internet vạn vật", "IoT (Internet of Things)", "Kết nối thiết bị thông minh để thu thập, trao đổi, xử lí dữ liệu"],
    ["Trí tuệ nhân tạo / Dữ liệu lớn", "AI / Big Data", "Trí tuệ nhân tạo / Dữ liệu lớn"],
    ["Phần mềm độc hại", "malware", "Virus, worm, trojan, spyware, ransomware…"],
    ["Bản quyền / Quyền tác giả", "Copyright (©)", "Quyền tác giả đối với tác phẩm"],
    ["Học liệu mở", "OER (Open Educational Resources)", "Tài nguyên giáo dục mở, dùng được hợp pháp"],
    ["Xác thực 2 yếu tố", "2FA", "Bảo vệ tài khoản bằng thêm một lớp mã xác thực"],
], [135, 135, 195], font="cellsm"))
story.append(PageBreak())

# ==========================================================================
# PHAN IV - 100% YEU CAU CAN DAT -> CAU HOI & DAP AN MAU
# ==========================================================================
# Moi phan tu: (ma, don vi, muc do, yeu cau can dat (nguyen van/rut gon),
#               cau hoi, dap an mau, vi tri ly thuyet, cau luyen tap lien quan)
REQUIREMENTS = [
 ("A1-NB-1", "A1", "Nhận biết", "Nêu được sự ưu việt của việc lưu trữ dựa trên các thiết bị số.",
  "Hãy nêu ít nhất năm ưu việt của việc lưu trữ thông tin bằng thiết bị số so với việc lưu trữ trên giấy.",
  "Thiết bị số lưu được lượng dữ liệu khổng lồ trên kích thước rất nhỏ gọn; truy xuất và tìm kiếm cực nhanh; sao chép hàng triệu lần không suy giảm chất lượng, không bị ố vàng hay rách; dễ sửa đổi, sắp xếp, nén và mã hoá; dễ chia sẻ, truyền đi xa qua mạng trong vài giây với chi phí thấp; dễ sao lưu nhiều bản ở nhiều nơi; tiết kiệm chi phí in ấn, kho bãi và nhân công. Ngoài ra có thể dùng dịch vụ điện toán đám mây với sức chứa gần như không giới hạn.",
  "II.1.1c", "TN 1–4, TL 1"),
 ("A1-TH-1", "A1", "Thông hiểu", "Phân biệt được thông tin và dữ liệu.",
  "Thông tin khác dữ liệu ở điểm nào? Hãy giải thích mối quan hệ giữa chúng.",
  "Thông tin là tất cả những gì mang lại sự hiểu biết cho con người, gắn với quá trình nhận thức và có thể làm thay đổi hành động. Dữ liệu là thông tin đã được đưa vào máy tính, được biểu diễn thành chữ, số, hình ảnh, âm thanh, video… để máy tính nhận biết và xử lí được. Dữ liệu là nguyên liệu thô (đầu vào), thông tin là ý nghĩa thu được sau xử lí (đầu ra). Trong máy tính, xử lí thông tin chính là xử lí dữ liệu; cùng một dữ liệu có thể cho thông tin khác nhau tuỳ hiểu biết của người nhận.",
  "II.1.1a", "TN 5–8, ĐS 1"),
 ("A1-TH-2", "A1", "Thông hiểu", "Nêu được ví dụ minh hoạ về thông tin và dữ liệu.",
  "Hãy cho một ví dụ cụ thể phân biệt dữ liệu và thông tin.",
  "Dãy số «37; 39; 40; 38; 41» ghi trong tệp «nhietdo.txt» là dữ liệu. Sau khi chương trình tính trung bình và so sánh với ngưỡng, máy tính đưa ra kết quả «nhiệt độ cơ thể 39 °C – bạn đang sốt cao, cần đến bác sĩ»: đó là thông tin. Ví dụ khác: tệp ảnh «anh.jpg» là dữ liệu; khi xem ảnh và nhận ra «đây là Chùa Cầu ở Hội An» thì bạn đã nhận được thông tin.",
  "II.1.1a", "TN 9–10"),
 ("A1-VD-1", "A1", "Vận dụng", "Chuyển đổi được giữa các đơn vị lưu trữ thông tin: B, KB, MB,…",
  "Hãy thực hiện các phép đổi sau: 3 MB = ? KB; 2 GB = ? KB; 2 048 B = ? KB; 3 MB = ? bit.",
  "Dùng 1 B = 8 bit và cứ mỗi bậc hơn kém 2¹⁰ = 1 024 lần. (1) 3 MB = 3 × 1 024 = 3 072 KB. (2) 2 GB = 2 × 1 024 MB = 2 048 MB = 2 048 × 1 024 = 2 097 152 KB. (3) 2 048 B = 2 048 : 1 024 = 2 KB. (4) 3 MB = 3 × 1 024 × 1 024 B = 3 145 728 B; nhân 8 → 25 165 824 bit. Nhớ: từ đơn vị lớn xuống nhỏ thì nhân, từ nhỏ lên lớn thì chia.",
  "III.1", "TN 11–16, TL 2, Đề thử TL 1"),
 ("A1-VD-2", "A1", "Vận dụng", "Xử lí và truyền thông tin bằng thiết bị số.",
  "Em hãy mô tả cách một chiếc điện thoại thông minh xử lí và truyền một bức ảnh cho bạn bè.",
  "Bước 1 (tiếp nhận dữ liệu): camera thu ánh sáng, cảm biến chuyển thành dữ liệu số, máy lưu thành tệp «IMG_001.jpg». Bước 2 (xử lí): phần mềm nén ảnh, gắn thông tin thời gian, địa điểm, lưu vào bộ nhớ. Bước 3 (đưa ra kết quả và truyền): màn hình hiển thị ảnh; khi bấm Gửi, điện thoại dùng wifi/4G/5G và giao thức TCP/IP để truyền tệp qua Internet tới máy chủ của ứng dụng nhắn tin, rồi tới máy bạn bè – nơi ảnh được giải nén và hiển thị. Như vậy thiết bị số vừa xử lí vừa truyền thông tin.",
  "II.1.1b", "TN 17–18, TL 3"),
 ("A2-NB-1", "A2", "Nhận biết", "Trình bày được những đóng góp cơ bản của tin học đối với xã hội.",
  "Tin học đã đóng góp những gì cơ bản cho xã hội? Hãy trình bày ngắn gọn.",
  "Năm nhóm đóng góp lớn: (1) Quản lí – xử lí nghiệp vụ nhanh, chính xác, tiết kiệm (quản lí học sinh, ngân hàng, bán hàng); (2) Tự động hoá – rô-bốt, thiết bị thông minh thay con người trong môi trường lặp lại hoặc nguy hiểm; (3) Giải quyết bài toán khoa học – kĩ thuật – tính toán, mô phỏng, dự báo thời tiết, giải mã gen; (4) Thay đổi cách thức làm việc – làm việc trực tuyến, thương mại điện tử, thanh toán không dùng tiền mặt; (5) Giao tiếp cộng đồng – thư điện tử, mạng xã hội, diễn đàn. Ngoài ra còn đóng góp cho giáo dục, y tế, giải trí.",
  "II.1.2c", "TN 19–22, TL 4"),
 ("A2-NB-2", "A2", "Nhận biết", "Nhận biết được một vài thiết bị số thông dụng khác ngoài máy tính để bàn và laptop.",
  "Ngoài máy tính để bàn và laptop, hãy kể tên ít nhất sáu thiết bị số thông dụng.",
  "Điện thoại thông minh, máy tính bảng, đồng hồ thông minh, tivi thông minh (smart TV), loa thông minh, camera an ninh IP, robot hút bụi, công tơ điện tử, máy ảnh số, thẻ nhớ/USB, đầu thu phát wifi, thẻ RFID thu phí không dừng, thiết bị đeo tay theo dõi sức khoẻ, xe tự hành. Các thiết bị này đều lưu trữ, xử lí hoặc truyền dữ liệu dưới dạng số.",
  "II.1.2a", "TN 23–26"),
 ("A2-NB-3", "A2", "Nhận biết", "Giới thiệu được các thành tựu nổi bật ở một số mốc thời gian để minh hoạ sự phát triển của ngành tin học.",
  "Hãy nêu ít nhất bốn mốc thời gian với thành tựu tiêu biểu của ngành tin học và ý nghĩa của chúng.",
  "1957: ngôn ngữ lập trình bậc cao FORTRAN ra đời, giúp lập trình viên mô tả thuật toán thay vì viết mã máy. 1964: hệ điều hành OS/360 trên dòng IBM/360 đặt nền móng cho hệ điều hành hiện đại. 1969–1983: ARPANET ra đời và TCP/IP được thiết lập (1983) tạo nền tảng cho Internet. 1971: bộ vi xử lí Intel 4004 mở đường cho máy tính cá nhân; 1981: IBM PC phổ biến máy tính cá nhân. 1989–1992: World Wide Web ra đời giúp Internet bùng nổ. 2007: điện thoại thông minh mở kỉ nguyên Internet di động. Thập niên 2010 đến nay: AI, Big Data, điện toán đám mây, IoT và CMCN 4.0.",
  "II.1.2d", "TN 27–30, ĐS 2"),
 ("A2-TH-1", "A2", "Thông hiểu", "Nêu được ví dụ cụ thể về thiết bị thông minh.",
  "Hãy cho ba ví dụ về thiết bị thông minh và chỉ ra điểm «thông minh» của mỗi thiết bị.",
  "Đồng hồ thông minh: có cảm biến nhịp tim, tự đo và gửi dữ liệu về điện thoại qua bluetooth, tự nhắc bạn vận động. Tivi thông minh: chạy hệ điều hành, kết nối Internet, cài được ứng dụng xem phim và nghe lệnh giọng nói. Robot hút bụi: dùng cảm biến để lập bản đồ phòng, tự tính đường đi, tự tránh vật cản và tự về trạm sạc. Điểm chung: hoạt động tự chủ nhờ phần mềm và có khả năng kết nối để thu nhận – xử lí – truyền dữ liệu.",
  "II.1.2a", "TN 31–33, ĐS 2"),
 ("A2-TH-2", "A2", "Thông hiểu", "Giải thích được vai trò của những thiết bị thông minh đối với sự phát triển của xã hội và cuộc cách mạng công nghiệp 4.0.",
  "Vì sao thiết bị thông minh được coi là thành phần chủ chốt của cuộc cách mạng công nghiệp 4.0?",
  "CMCN 4.0 dựa trên công nghệ số, kết hợp AI, IoT, điện toán đám mây và dữ liệu lớn để tạo ra sản xuất thông minh, làm mờ ranh giới giữa hệ thống thực và hệ thống ảo. Thiết bị thông minh có cảm biến thu thập dữ liệu tự động, liên tục, tức thời trên diện rộng, truyền về trung tâm để AI phân tích rồi tự động điều khiển lại thiết bị. Chúng là «giác quan và tay chân» của mọi hệ thống IoT: từ nhà thông minh, công tơ điện tử, camera giao thông đến dây chuyền sản xuất tự động. Nhờ đó năng suất tăng, chi phí giảm, quyết định chính xác hơn và nền kinh tế tri thức được thúc đẩy.",
  "II.1.2e", "TN 34–35, TL 5"),
 ("A2-TH-3", "A2", "Thông hiểu", "Giải thích được các thiết bị đó cũng là những hệ thống xử lí thông tin.",
  "Hãy chứng minh một thiết bị thông minh (ví dụ điện thoại) cũng là một hệ thống xử lí thông tin.",
  "Một hệ thống xử lí thông tin gồm đầu vào – xử lí – lưu trữ – đầu ra/truyền thông. Điện thoại thông minh có: đầu vào (micro, camera, cảm biến vân tay, GPS, màn hình cảm ứng); bộ xử lí và phần mềm (chip, hệ điều hành Android/iOS, ứng dụng); bộ nhớ (RAM, bộ nhớ trong, đám mây); đầu ra (màn hình, loa, rung) và khả năng truyền dữ liệu qua wifi/4G/5G/bluetooth. Vì vậy nó thực hiện đầy đủ 3 bước: tiếp nhận dữ liệu → xử lí dữ liệu → đưa ra kết quả, đồng thời lưu trữ và truyền thông tin.",
  "II.1.2b", "TN 36–37, ĐS 2"),
 ("A2-TH-4", "A2", "Thông hiểu", "Nêu được ví dụ minh họa về những đóng góp cơ bản của tin học đối với xã hội.",
  "Hãy cho ví dụ minh hoạ đóng góp của tin học trong ba lĩnh vực: giáo dục, y tế và giao tiếp cộng đồng.",
  "Giáo dục: học sinh học trực tuyến qua Zoom/Google Meet, đọc bài giảng điện tử, tra cứu thư viện số và luyện tập bằng ứng dụng học tiếng Anh. Y tế: bệnh án điện tử giúp bác sĩ tra cứu nhanh, khám chữa bệnh từ xa (telemedicine), đặt lịch khám và khai báo y tế trực tuyến. Giao tiếp cộng đồng: thư điện tử, nhóm chat Zalo, mạng xã hội giúp mọi người chia sẻ thông tin, phản hồi ngay lập tức dù ở xa nhau. Các ví dụ này cho thấy tin học làm tăng tốc độ, độ chính xác và khả năng tiếp cận dịch vụ.",
  "II.1.2c", "TN 38, TL 4"),
 ("A3-VD-1", "A3", "Vận dụng", "Khởi động được một số thiết bị số thông dụng.",
  "Em hãy mô tả các bước khởi động và đăng nhập an toàn trên một chiếc laptop (hoặc điện thoại).",
  "Bước 1: kiểm tra nguồn điện/pin, nhấn nút nguồn. Bước 2: chờ hệ điều hành (Windows/macOS/Linux hoặc Android/iOS) nạp xong, không bấm phím liên tục. Bước 3: trên màn hình đăng nhập, nhập đúng mật khẩu / mã PIN hoặc dùng vân tay, khuôn mặt; chú ý không để người khác nhìn thấy. Bước 4: kiểm tra nhanh kết nối mạng và thông báo cập nhật. Bước 5: mở ứng dụng cần dùng; khi kết thúc, đăng xuất tài khoản và dùng lệnh Shut down/Restart thay vì rút điện đột ngột. Với điện thoại, thao tác tương tự: giữ nút nguồn → mở khoá màn hình bằng sinh trắc học/mã PIN.",
  "II.1.3", "TN 39, TL 6"),
 ("A3-VD-2", "A3", "Vận dụng", "Sử dụng được các tệp dữ liệu, các chức năng và phần mềm ứng dụng cơ bản cài sẵn trên các thiết bị đó.",
  "Em cần tạo thư mục, lưu tệp bài học, mở bằng phần mềm phù hợp rồi chia sẻ cho bạn. Hãy trình bày các thao tác.",
  "Mở trình quản lí tệp (File Explorer / Files) → tạo thư mục «Tin_hoc_10» trong Documents → tải tệp «bai1.pdf» về rồi sao chép/di chuyển vào thư mục, đặt tên rõ ràng không dấu → nháy đúp để mở bằng trình đọc PDF (hoặc chọn «Mở bằng» → trình soạn thảo/bảng tính tương ứng với .docx, .xlsx) → dùng chức năng ghi chú/tô sáng nội dung chính → lưu lại (Ctrl+S) → nháy chuột phải chọn «Chia sẻ» hoặc tải lên Google Drive, đặt quyền «Chỉ xem» và gửi liên kết cho bạn. Cuối cùng quét virus nhanh và sao lưu tệp quan trọng.",
  "II.1.3", "TN 40, TL 6"),
 ("B1-NB-1", "B1", "Nhận biết", "Nêu được một số dịch vụ cụ thể mà Điện toán đám mây cung cấp cho người dùng.",
  "Hãy kể tên ít nhất bốn dịch vụ cụ thể của điện toán đám mây và cho biết mỗi dịch vụ thuộc loại nào.",
  "Các dịch vụ phổ biến: lưu trữ và đồng bộ dữ liệu Google Drive, Dropbox, OneDrive (IaaS); thư điện tử Gmail (SaaS); soạn thảo văn bản trực tuyến Google Docs, Microsoft 365 (SaaS); họp trực tuyến Zoom, Google Meet (SaaS); máy chủ ảo Amazon EC2, Azure VM (IaaS); nền tảng phát triển ứng dụng Google App Engine (PaaS); sao lưu ảnh tự động iCloud/Google Photos. Điểm chung: người dùng đăng kí tài khoản, truy cập tài nguyên qua Internet và trả phí theo mức sử dụng.",
  "II.2.1d", "TN 41–45, ĐS 3"),
 ("B1-NB-2", "B1", "Nhận biết", "Nêu được khái niệm Internet vạn vật (IoT).",
  "Internet vạn vật (IoT) là gì? Hãy viết đầy đủ thuật ngữ tiếng Anh.",
  "IoT viết đầy đủ là Internet of Things – Internet vạn vật. Đây là việc liên kết các thiết bị thông minh (được gắn cảm biến, cài phần mềm chuyên dụng) với nhau qua mạng để tự động thu thập, trao đổi và xử lí dữ liệu phục vụ các mục đích khác nhau, không nhất thiết có sự tương tác trực tiếp giữa người với người hay người với máy tính. Các thiết bị có thể kết nối qua Internet, LAN, bluetooth, RFID; khi tích hợp AI chúng còn tự đưa ra quyết định.",
  "II.2.1e", "TN 46–48, ĐS 3"),
 ("B1-TH-1", "B1", "Thông hiểu", "Trình bày được những thay đổi về chất lượng cuộc sống, phương thức học tập và làm việc trong xã hội mà ở đó mạng máy tính được sử dụng phổ biến.",
  "Mạng máy tính và Internet đã làm thay đổi chất lượng cuộc sống, học tập và làm việc như thế nào?",
  "Về chất lượng cuộc sống: mua sắm, thanh toán, đặt vé, giải trí, khám bệnh từ xa và thủ tục hành chính trực tuyến trở nên nhanh chóng, tiện lợi. Về học tập: Internet là nguồn học liệu khổng lồ; nền tảng học trực tuyến, bài giảng điện tử và học liệu mở giúp học mọi lúc, mọi nơi, học suốt đời. Về làm việc: họp trực tuyến, làm việc từ xa, cộng tác trên tài liệu đám mây và chia sẻ dữ liệu tức thời giúp tăng năng suất, giảm chi phí đi lại. Bên cạnh lợi ích, còn có mặt trái: tin giả, lừa đảo, nghiện mạng, lộ dữ liệu cá nhân nên mỗi người cần kĩ năng tự bảo vệ.",
  "II.2.1f", "TN 49–50, TL 7"),
 ("B1-TH-2", "B1", "Thông hiểu", "So sánh được mạng LAN và Internet.",
  "Hãy so sánh mạng LAN và Internet theo ít nhất bốn tiêu chí.",
  "(1) Phạm vi: LAN trong phạm vi nhỏ (nhà, trường, cơ quan); Internet là mạng toàn cầu. (2) Kết nối: LAN dùng Switch/Hub/wifi nội bộ và đường truyền riêng; Internet nối các LAN qua Router và đường truyền của ISP (Viettel, VNPT, FPT…). (3) Sở hữu: LAN thuộc sở hữu và quản lí của một tổ chức; Internet không thuộc sở hữu của riêng ai, chỉ có tổ chức điều phối tên miền, địa chỉ IP và tiêu chuẩn. (4) Tốc độ/độ trễ: LAN thường cao, ổn định; Internet phụ thuộc nhà mạng. (5) Rủi ro: LAN dễ kiểm soát; Internet tiềm ẩn nhiều nguy cơ về an toàn thông tin.",
  "II.2.1c", "TN 51–53, ĐS 3"),
 ("B1-TH-3", "B1", "Thông hiểu", "Nêu được ví dụ cụ thể về thay đổi trong cuộc sống mà IoT đem lại. Phát biểu ý kiến cá nhân về lợi ích của IoT.",
  "Hãy nêu hai ví dụ về thay đổi do IoT đem lại và trình bày ý kiến cá nhân về lợi ích của IoT.",
  "Ví dụ 1: thu phí không dừng trên cao tốc – thẻ RFID trên kính xe được thiết bị đọc tự động, dữ liệu gửi về trung tâm để trừ tiền và mở barie, xe không phải dừng, giảm ùn tắc. Ví dụ 2: công tơ điện tử thông minh – số điện năng được đo liên tục và gửi tự động về công ty điện, không còn nhân viên đi ghi chỉ số, số liệu chính xác hơn. Ý kiến cá nhân: theo em, lợi ích lớn nhất của IoT là cung cấp dữ liệu đúng, đủ, kịp thời để con người và máy móc quyết định nhanh hơn, tiết kiệm nhân lực, nâng cao an toàn và tiện nghi. Tuy nhiên cần chú ý bảo mật thiết bị, mã hoá dữ liệu và tôn trọng quyền riêng tư, nếu không IoT có thể trở thành công cụ theo dõi người dùng.",
  "II.2.1e", "TN 54–55, TL 8"),
 ("B2-NB-1", "B2", "Nhận biết", "Trình bày được sơ lược về phần mềm độc hại.",
  "Phần mềm độc hại là gì? Hãy nêu tên và đặc điểm của ba loại chính.",
  "Phần mềm độc hại (malware) là phần mềm được viết với ý đồ xấu, gây hại cho người dùng, thiết bị hoặc dữ liệu. Ba loại chính: (1) Virus – chỉ là đoạn mã độc, không phải chương trình hoàn chỉnh, phải gắn vào chương trình khác để phát tác và lây lan qua trao đổi tệp, USB; (2) Worm – chương trình hoàn chỉnh, tự phát tán qua mạng bằng cách lợi dụng lỗ hổng hệ điều hành hoặc lừa người dùng mở liên kết/email (Melissa, Code Red, WannaCry); (3) Trojan – ngụy trang thành phần mềm hữu ích, ít chú trọng lây lan, chuyên ăn cắp thông tin và chiếm quyền điều khiển (spyware, keylogger, backdoor, rootkit). Ngoài ra còn có ransomware, adware, phishing.",
  "II.2.2c", "TN 56–60, ĐS 4"),
 ("B2-NB-2", "B2", "Nhận biết", "Nêu được một vài cách phòng vệ khi bị bắt nạt trên mạng.",
  "Nếu bị bắt nạt trên mạng, em nên làm gì? Hãy nêu ít nhất bốn cách phòng vệ.",
  "Không trả lời, không tranh luận và không đáp trả kẻ bắt nạt; không kết bạn dễ dãi với người lạ và không nhận lời mời vào nhóm lạ. Lưu giữ toàn bộ bằng chứng (chụp màn hình, lưu tin nhắn, ghi thời gian, tên tài khoản). Chia sẻ ngay với bố mẹ, thầy cô hoặc người lớn đáng tin cậy, không im lặng chịu đựng. Sử dụng chức năng chặn (block), ẩn bình luận và báo cáo vi phạm cho nền tảng. Khi bị đe doạ, tống tiền hoặc phát tán thông tin nhạy cảm, báo cơ quan công an kèm theo bằng chứng. Đồng thời chăm sóc sức khoẻ tinh thần, không tự cô lập.",
  "II.2.2d", "TN 61–63, ĐS 4"),
 ("B2-NB-3", "B2", "Nhận biết", "Nêu được những nguy cơ và tác hại nếu tham gia các hoạt động trên Internet một cách bất cẩn và thiếu hiểu biết.",
  "Kể tên ít nhất năm nguy cơ khi tham gia Internet thiếu hiểu biết và nêu tác hại tương ứng.",
  "(1) Tin giả, tin phản văn hoá → nhận thức lệch lạc, hoang mang, hành xử sai; (2) Lừa đảo (trang mạo danh, việc nhẹ lương cao, đầu tư tiền ảo) → mất tiền, mất tài khoản; (3) Lộ thông tin cá nhân (CCCD, số điện thoại, tài khoản ngân hàng, OTP) → bị mạo danh, tống tiền, mất tiền; (4) Bắt nạt trên mạng → tổn thương tâm lí, trầm cảm, tự cô lập; (5) Nghiện mạng/game → suy giảm sức khoẻ và kết quả học tập; (6) Phần mềm độc hại khi tải phần mềm lậu hoặc mở link lạ → mất dữ liệu, máy bị chiếm quyền, bị tống tiền.",
  "II.2.2b", "TN 64–66, ĐS 4"),
 ("B2-TH-1", "B2", "Thông hiểu", "Trình bày được một số cách đề phòng những tác hại khi tham gia các hoạt động trên Internet.",
  "Hãy trình bày sáu biện pháp đề phòng các tác hại khi tham gia Internet.",
  "Chỉ truy cập trang web tin cậy (https://, có tên miền rõ ràng) và kiểm chứng thông tin từ nhiều nguồn trước khi tin, trước khi chia sẻ. Không công khai thông tin cá nhân, không gửi OTP/mật khẩu cho ai. Đặt mật khẩu mạnh, khác nhau cho từng tài khoản, bật xác thực 2 yếu tố và thay đổi định kì. Không mở liên kết, tệp đính kèm lạ; xác minh lại qua điện thoại nếu người quen gửi link bất thường. Không tải phần mềm bẻ khoá; cài và cập nhật phần mềm diệt virus, cập nhật hệ điều hành, quét USB/thẻ nhớ trước khi mở. Sao lưu dữ liệu quan trọng. Cuối cùng, giữ thái độ ứng xử văn minh, không tham gia phát tán tin giả hay bình luận ác ý.",
  "II.2.2c, e", "TN 67–70, TL 9"),
 ("B2-VD-1", "B2", "Vận dụng", "Sử dụng được một số công cụ thông dụng để ngăn ngừa và loại bỏ phần mềm độc hại.",
  "Em hãy hướng dẫn bạn bè quét virus cho máy tính Windows bằng Windows Defender.",
  "Mở Start → Settings (hoặc gõ «Defender» vào ô tìm kiếm) → Windows Security → «Virus & threat protection» (Bảo vệ chống virus và các nguy cơ). Xem mục Current threats để biết nguy cơ gần đây. Bấm «Scan options» → chọn kiểu quét: Quick scan (vùng nguy cơ cao, nhanh), Full scan (toàn bộ ổ đĩa, lâu hơn), Custom scan (chỉ định thư mục), Windows Defender Offline scan (mã độc khó gỡ, khởi động lại máy). Bấm «Scan now», đợi kết quả và làm theo khuyến nghị (cách li/xoá mối đe doạ). Với một tệp hoặc thư mục cụ thể, chỉ cần nháy chuột phải → «Scan with Microsoft Defender». Ngoài ra có thể dùng BKAV, Kaspersky, Avast… và nhớ cập nhật mẫu virus thường xuyên.",
  "II.2.2c", "TN 71–72, TL 10"),
 ("B2-VD-2", "B2", "Vận dụng", "Sử dụng được một số chức năng xử lí thông tin trên máy PC và thiết bị số, ví dụ dịch tự động văn bản hay tiếng nói.",
  "Hãy mô tả cách dùng công cụ dịch tự động để dịch một đoạn văn bản tiếng Anh sang tiếng Việt, và cách dùng tính năng nhận dạng tiếng nói.",
  "Dịch văn bản: mở trình duyệt, truy cập translate.google.com (hoặc ứng dụng dịch) → chọn ngôn ngữ nguồn «English» và ngôn ngữ đích «Vietnamese» → nhập hoặc dán đoạn văn bản/ tải tệp → đọc bản dịch hiển thị ngay lập tức → rà soát, sửa thuật ngữ chưa đúng → sao chép và ghi rõ nguồn nếu dùng trong bài làm. Nhận dạng tiếng nói: bật chế độ micro/voice input trên điện thoại hoặc trong ứng dụng ghi chú → cho phép quyền dùng micro → nói rõ từng câu → kiểm tra văn bản được chuyển đổi → sửa lỗi chính tả → lưu hoặc gửi. Cần lưu ý bản dịch máy chỉ là tham khảo, phải kiểm tra lại trước khi dùng chính thức.",
  "II.2.2a", "TN 73–74, TL 3"),
 ("B2-VD-3", "B2", "Vận dụng", "Khai thác được một số nguồn học liệu mở trên Internet.",
  "Học liệu mở là gì? Hãy nêu quy trình tìm và sử dụng hợp pháp một nguồn học liệu mở.",
  "Học liệu mở (OER – Open Educational Resources) là tài nguyên giáo dục được chia sẻ miễn phí, cho phép người học sử dụng, chỉnh sửa và chia sẻ lại hợp pháp, thường kèm giấy phép Creative Commons (CC). Quy trình: (1) xác định nội dung cần học, dùng máy tìm kiếm với từ khoá + «OER»/«Creative Commons»/«bài giảng điện tử»; (2) ưu tiên nguồn uy tín như Khan Academy, MIT OpenCourseWare, thư viện số của trường đại học, cổng bài giảng điện tử của Bộ GDĐT; (3) đọc kĩ giấy phép (có được phép sửa? có phải ghi nguồn? có bị cấm dùng thương mại?); (4) tải về hoặc xem trực tuyến, ghi chép có chọn lọc; (5) khi dùng lại trong bài làm, ghi rõ tên tác giả, tên tài liệu, địa chỉ nguồn và ngày truy cập. Nhờ học liệu mở, em có thể học mọi lúc, mọi nơi mà vẫn tôn trọng bản quyền.",
  "II.2.2a", "TN 75–76, TL 11"),
 ("B2-VD-4", "B2", "Vận dụng", "Biết cách tự bảo vệ dữ liệu của cá nhân.",
  "Em hãy liệt kê ít nhất sáu cách tự bảo vệ dữ liệu cá nhân trong môi trường số.",
  "Đặt mật khẩu mạnh (dài, gồm chữ hoa, chữ thường, số, kí hiệu), dùng mật khẩu khác nhau cho mỗi tài khoản và thay đổi định kì. Bật xác thực 2 yếu tố; tuyệt đối không chia sẻ mật khẩu và mã OTP. Không đăng công khai CCCD, số điện thoại, địa chỉ, lịch trình, tài khoản ngân hàng; cài chế độ riêng tư cho mạng xã hội. Không để chế độ «ghi nhớ mật khẩu» trên máy công cộng, luôn đăng xuất sau khi dùng và tránh đăng nhập qua wifi công cộng không mã hoá. Chỉ cấp cho ứng dụng những quyền thật sự cần thiết; gỡ ứng dụng không rõ nguồn. Cập nhật hệ điều hành, dùng phần mềm diệt virus và sao lưu dữ liệu định kì theo quy tắc 3-2-1.",
  "II.2.2e", "TN 77–80, TL 12"),
 ("D-NB-1", "D", "Nhận biết", "Nêu được một số vấn đề nảy sinh về pháp luật, đạo đức, văn hoá khi việc giao tiếp qua mạng trở nên phổ biến.",
  "Giao tiếp qua mạng phổ biến làm nảy sinh những vấn đề gì về pháp luật, đạo đức và văn hoá?",
  "Về pháp luật: vi phạm bản quyền (copy nhạc, phim, phần mềm, bài viết), đăng tin sai sự thật/vu khống, lộ bí mật nhà nước và dữ liệu cá nhân, lừa đảo, phát tán mã độc, kinh doanh hàng cấm. Về đạo đức: nói dối, mạo danh, lợi dụng lòng tốt, gian lận học tập, «xào» nội dung của người khác, phát tán ảnh riêng tư. Về văn hoá: ngôn từ thô tục, xúc phạm danh dự nhân phẩm, kì thị, bình luận ác ý, phát tán nội dung bạo lực, đồi truỵ, thiếu tôn trọng trong giao tiếp. Các vấn đề này đòi hỏi mỗi công dân số vừa hiểu luật, vừa ứng xử có văn hoá và đạo đức.",
  "II.3.1a", "TN 81–83, ĐS 5"),
 ("D-NB-2", "D", "Nhận biết", "Trình bày được một số nội dung cơ bản của Luật Công nghệ thông tin, Nghị định về quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin, Luật An ninh mạng.",
  "Hãy trình bày nội dung cơ bản của ba văn bản pháp luật được học trong Chủ đề D.",
  "(1) Luật Công nghệ thông tin số 67/2006/QH11: quy định hoạt động ứng dụng, phát triển CNTT; Điều 12 liệt kê các hành vi bị cấm, trong đó khoản 2 cấm cung cấp, trao đổi, truyền đưa, lưu trữ, sử dụng thông tin số nhằm chống Nhà nước, kích động bạo lực, xuyên tạc, vu khống, xúc phạm uy tín tổ chức, danh dự nhân phẩm công dân… (2) Nghị định 72/2013/NĐ-CP (sửa đổi bởi Nghị định 27/2018/NĐ-CP) về quản lí, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng: quy định điều kiện cung cấp dịch vụ, quản lí trang thông tin điện tử, mạng xã hội, trò chơi trực tuyến; Điều 5 nêu các hành vi bị cấm trên mạng. (3) Luật An ninh mạng số 24/2018/QH14 (hiệu lực 1/1/2019): bảo vệ an ninh quốc gia trên không gian mạng; Điều 8 khoản 1 nghiêm cấm dùng không gian mạng để đưa thông tin sai sự thật gây hoang mang, xuyên tạc lịch sử, đăng nội dung dâm ô, xúc phạm tôn giáo, xâm phạm quyền lợi hợp pháp của tổ chức, cá nhân.",
  "II.3.1c", "TN 84–86, ĐS 5"),
 ("D-TH-1", "D", "Thông hiểu", "Nêu được ví dụ minh họa sự vi phạm bản quyền thông tin và sản phẩm số. Giải thích được sự vi phạm đã diễn ra như thế nào và có thể dẫn tới hậu quả gì.",
  "Bạn Nam tải một bài hát đang nổi trên YouTube rồi đăng lại lên kênh của mình để lấy view. Hãy phân tích hành vi và hậu quả.",
  "Đây là hành vi vi phạm bản quyền. Diễn biến: bài hát là tác phẩm thuộc quyền tác giả của nhạc sĩ/nhà sản xuất; Nam tự ý sao chép (tải về), phân phối và truyền đạt tác phẩm tới công chúng qua mạng mà không có sự cho phép và không trả phí bản quyền – thuộc các hành vi xâm phạm quyền tác giả theo Điều 28 Luật Sở hữu trí tuệ. Hậu quả: kênh của Nam có thể bị gỡ video, bị khoá tính năng kiếm tiền; Nam phải xin lỗi, bồi thường thiệt hại cho chủ sở hữu; có thể bị xử phạt hành chính theo Nghị định 131/2013/NĐ-CP (hành vi sao chép tác phẩm trái phép bị phạt 15–35 triệu đồng), thậm chí bị truy cứu trách nhiệm hình sự nếu vi phạm nghiêm trọng, chưa kể mất uy tín cá nhân.",
  "II.3.1b", "TN 87–88, TL 13"),
 ("D-TH-2", "D", "Thông hiểu", "Giải thích được một số nội dung cơ bản của Luật Công nghệ thông tin, Nghị định về quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin, Luật An ninh mạng. Nêu được ví dụ minh họa.",
  "Hãy giải thích một điều cấm của Luật An ninh mạng và cho ví dụ minh hoạ cụ thể.",
  "Điểm d khoản 1 Điều 8 Luật An ninh mạng 2018 nghiêm cấm sử dụng không gian mạng để đưa thông tin sai sự thật gây hoang mang trong nhân dân, gây thiệt hại cho hoạt động kinh tế – xã hội, xâm hại quyền và lợi ích hợp pháp của tổ chức, cá nhân. Giải thích: khi một người đăng tin bịa đặt, dù chỉ «nghe nói», nhưng nội dung đó lan truyền nhanh trên mạng xã hội, gây hoang mang dư luận hoặc làm thiệt hại cho doanh nghiệp, thì hành vi đã xâm phạm trật tự thông tin trên không gian mạng. Ví dụ: tháng 3/2020, một tài khoản Facebook chia sẻ tin «TP. HCM sẽ phong toả 14 ngày» sai sự thật, gây hoang mang, người dân đi mua hàng dự trữ. Hành vi này bị nghiêm cấm theo Luật An ninh mạng và có thể bị phạt 10–20 triệu đồng theo khoản 1 Điều 101 Nghị định 15/2020/NĐ-CP, kèm buộc gỡ bỏ thông tin.",
  "II.3.1c", "TN 89–90, TL 14"),
 ("D-TH-3", "D", "Thông hiểu", "Giải thích được một số khía cạnh pháp lí của vấn đề bản quyền, của việc sở hữu, sử dụng và trao đổi thông tin trong môi trường số. Nêu được ví dụ minh hoạ.",
  "Hãy phân tích khía cạnh pháp lí của việc sở hữu, sử dụng và trao đổi thông tin số, kèm ví dụ.",
  "Về sở hữu: tác phẩm số (bài viết, ảnh, nhạc, phần mềm, website) thuộc quyền tác giả của người sáng tạo hoặc tổ chức được chuyển giao quyền; kí hiệu © là tuyên bố bảo hộ. Về sử dụng: người dùng chỉ được sử dụng trong phạm vi giấy phép; Điều 25 Luật SHTT cho phép một số trường hợp dùng tác phẩm đã công bố mà không phải xin phép, không trả nhuận bút nếu trích dẫn hợp lí, không làm sai ý tác giả và ghi rõ nguồn. Về trao đổi: việc đăng tải, chia sẻ, nhân bản, truyền đạt tác phẩm qua mạng mà không có phép của chủ sở hữu là xâm phạm quyền tác giả (Điều 28) và có thể vi phạm Nghị định 72/2013/NĐ-CP. Ví dụ: một công ty lấy bài viết và video từ trang web của nhà sản xuất game nước ngoài đăng lên trang của mình mà không xin phép → vi phạm Luật SHTT, bị buộc gỡ bỏ và xử phạt theo Nghị định 131/2013/NĐ-CP. Ngược lại, học sinh trích một đoạn ngắn của bài báo, ghi rõ tên tác giả và đường dẫn nguồn để minh hoạ cho bài thuyết trình thì được phép.",
  "II.3.1b, c", "TN 91–93, TL 13"),
 ("D-TH-4", "D", "Thông hiểu", "Nêu được ví dụ về những tác hại của việc chia sẻ và phổ biến thông tin một cách bất cẩn.",
  "Hãy nêu hai ví dụ về tác hại của việc chia sẻ, phổ biến thông tin bất cẩn.",
  "Ví dụ 1: chia sẻ tin sai sự thật về dịch bệnh hoặc về một doanh nghiệp làm cho dư luận hoang mang, người dân đổ xô mua hàng, doanh nghiệp bị sụt giảm doanh thu; người chia sẻ có thể bị xử phạt theo Điều 101 Nghị định 15/2020/NĐ-CP. Ví dụ 2: đăng công khai ảnh chụp căn cước công dân, số điện thoại hay danh sách bạn bè trong một bài «thử thách» trên mạng xã hội, khiến kẻ xấu thu thập được thông tin để lập tài khoản giả mạo, lừa đảo vay tiền người thân hoặc tống tiền nạn nhân. Thêm một ví dụ nhỏ nhưng hay gặp: bấm Like/Share vào bài viết xúc phạm người khác cũng tiếp tay lan truyền nội dung độc hại, làm tổn thương nạn nhân và có thể bị xem xét trách nhiệm.",
  "II.3.1d", "TN 94–95, TL 14"),
 ("D-TH-5", "D", "Thông hiểu", "Nêu được một vài biện pháp đơn giản và thông dụng để nâng cao tính an toàn và hợp pháp của việc chia sẻ thông tin trong môi trường số.",
  "Hãy nêu ít nhất năm biện pháp để chia sẻ thông tin vừa an toàn vừa hợp pháp.",
  "Có hiểu biết cơ bản về quy định pháp luật về bản quyền, thông tin cá nhân và chia sẻ thông tin số. Kiểm chứng nguồn tin, đối chiếu với ít nhất hai nguồn uy tín trước khi like/share. Tôn trọng bản quyền sản phẩm thông tin của người khác: chỉ đăng nội dung tự tạo, có giấy phép hoặc trích dẫn hợp lí kèm tên tác giả, địa chỉ nguồn, ngày công bố. Không tuỳ tiện tiết lộ thông tin cá nhân của bản thân và của người khác. Dùng biện pháp an ninh: mật khẩu mạnh, xác thực 2 yếu tố, phần mềm diệt virus, cập nhật hệ điều hành; hạn chế đăng nhập trên máy lạ hoặc qua mạng không tin cậy, luôn đăng xuất. Khi phát hiện chia sẻ nhầm tin sai, lập tức gỡ bỏ, cải chính và thông báo cho người bị ảnh hưởng.",
  "II.3.1d", "TN 96–98, ĐS 5"),
 ("D-VDC-1", "D", "Vận dụng cao", "Vận dụng được Luật và Nghị định nêu trên để xác định được tính hợp pháp của một hành vi nào đó trong lĩnh vực quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin.",
  "Công ty A đăng thông tin sai sự thật về công ty B, làm B thiệt hại lớn về doanh thu. Hãy vận dụng các văn bản pháp luật đã học để xác định tính hợp pháp của hành vi của A và nêu cách xử lí.",
  "Bước 1 – Mô tả hành vi: công ty A sử dụng mạng/Internet để đăng tải và lan truyền thông tin sai sự thật về công ty B, gây thiệt hại kinh tế. Bước 2 – Đối chiếu văn bản: hành vi vi phạm điểm d khoản 1 Điều 8 Luật An ninh mạng số 24/2018/QH14 (cấm đưa thông tin sai sự thật gây hoang mang, xâm hại quyền và lợi ích hợp pháp của tổ chức, cá nhân); đồng thời thuộc hành vi bị cấm tại khoản 2 Điều 12 Luật Công nghệ thông tin 2006 (thông tin số xúc phạm uy tín của tổ chức) và Điều 5 Nghị định 72/2013/NĐ-CP (sửa đổi bởi Nghị định 27/2018/NĐ-CP) về thông tin trên mạng; chế tài xử phạt hành chính theo khoản 1 Điều 101 Nghị định 15/2020/NĐ-CP (10–20 triệu đồng). Bước 3 – Kết luận: hành vi của công ty A là KHÔNG HỢP PHÁP. Bước 4 – Xử lí: A phải gỡ bỏ thông tin sai, đăng cải chính xin lỗi công khai, bồi thường thiệt hại dân sự cho B theo Bộ luật Dân sự; có thể bị xử phạt hành chính, và nếu bịa đặt nhằm vu khống, xúc phạm danh dự nghiêm trọng thì có thể bị truy cứu trách nhiệm hình sự. Công ty B nên lưu bằng chứng (ảnh chụp màn hình, đường dẫn, thời gian) và gửi đơn tới cơ quan chức năng hoặc khởi kiện đòi bồi thường.",
  "II.3.1e", "ĐS 6, TL 15, Đề thử TL 3"),
]

# Dong bo cot "cau luyen tap" voi ngan hang cau hoi o Phan V (60 TN, 8 DS, 15 TL).
_PRACTICE_BY_UNIT = {
    "A1": "TN 1–8 · ĐS 1 · TL 1, 2",
    "A2": "TN 9–16 · ĐS 2 · TL 4, 5",
    "A3": "TN 17–18 · TL 6",
    "B1": "TN 19–28 · ĐS 3 · TL 7, 8",
    "B2": "TN 29–40 · ĐS 4 · TL 3, 9–12",
    "D":  "TN 41–60 · ĐS 5, 6 · TL 13–15",
}
_PRACTICE_SPECIAL = {
    "D-VDC-1": "ĐS 6 · TL 15 · Đề thử TL 3",
    "A1-VD-1": "TN 1–8 · TL 1, 2 · Đề thử TL 1",
    "B2-VD-1": "TN 29–40 · TL 10",
}
REQUIREMENTS = [
    (c, u, l, y, q, a, t, _PRACTICE_SPECIAL.get(c, _PRACTICE_BY_UNIT[u]))
    for (c, u, l, y, q, a, t, _p) in REQUIREMENTS
]

story.append(H1("PHẦN IV", "TOÀN BỘ YÊU CẦU CẦN ĐẠT → CÂU HỎI VÀ ĐÁP ÁN MẪU"))
story.append(P("Phần này là «xương sống» của đề cương: <b>mỗi yêu cầu cần đạt trong bản đặc tả gốc được chuyển thành đúng một câu hỏi kèm đáp án mẫu</b>. "
               "Có tất cả <b>35 câu</b>, đánh mã theo đơn vị kiến thức và mức độ nhận thức. "
               "Bảng đối chiếu ở Phụ lục B cho thấy không một yêu cầu nào bị bỏ sót."))
story.append(TB([
    ["Đơn vị", "Số câu hỏi", "Dải mã", "Mức độ"],
    ["A1. Dữ liệu, thông tin và xử lý thông tin", "5", "A1-NB-1 → A1-VD-2", "NB 1 · TH 2 · VD 2"],
    ["A2. Vai trò của máy tính và thiết bị thông minh", "7", "A2-NB-1 → A2-TH-4", "NB 3 · TH 4"],
    ["A3. Kĩ năng sử dụng thiết bị số", "2", "A3-VD-1 → A3-VD-2", "VD 2"],
    ["B1. Mạng máy tính, Internet, IoT", "5", "B1-NB-1 → B1-TH-3", "NB 2 · TH 3"],
    ["B2. Dịch vụ web, tự bảo vệ khi tham gia mạng", "8", "B2-NB-1 → B2-VD-4", "NB 3 · TH 1 · VD 4"],
    ["D. Nghĩa vụ tuân thủ pháp lí trong môi trường số", "8", "D-NB-1 → D-VDC-1", "NB 2 · TH 5 · VDC 1"],
], [180, 55, 125, 105], font="cellsm"))
current_unit = None
for code, unit, level, yccd, ques, ans, theory, practice in REQUIREMENTS:
    if unit != current_unit:
        current_unit = unit
        story.append(H2("IV." + str(["A1", "A2", "A3", "B1", "B2", "D"].index(unit) + 1) + ". " + {
            "A1": "Chủ đề A – Dữ liệu, thông tin và xử lý thông tin",
            "A2": "Chủ đề A – Vai trò của máy tính và thiết bị thông minh",
            "A3": "Chủ đề A – Kĩ năng sử dụng thiết bị số",
            "B1": "Chủ đề B – Mạng máy tính, Internet, IoT",
            "B2": "Chủ đề B – Dịch vụ web và tự bảo vệ khi tham gia mạng",
            "D": "Chủ đề D – Nghĩa vụ tuân thủ pháp lí trong môi trường số",
        }[unit]))
    story.append(QA(code, ques, ans, level))
    story.append(Spacer(1, 3))
story.append(BOX([P("<b>Nhận xét:</b> 35 câu trên phủ đúng 35 ý yêu cầu cần đạt của bản đặc tả. "
                    "Nếu em trả lời trọn vẹn được 35 câu này, em đã nắm 100% nội dung kiến thức của đề kiểm tra giữa kì I. "
                    "Hãy tiếp tục luyện thêm ở Phần V và làm đề thi thử ở Phần VI.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(PageBreak())

# ==========================================================================
# PHAN V - NGAN HANG CAU HOI LUYEN TAP (CO DAP AN & GIAI THICH)
# ==========================================================================
TN_BANK = [
 (1, "Đơn vị lưu trữ dữ liệu nhỏ nhất trong máy tính là gì?",
  {"A": "GB", "B": "MB", "C": "KB", "D": "Bit"}, "D",
  "Bit (0 hoặc 1) là đơn vị nhỏ nhất; 1 Byte = 8 bit."),
 (2, "Một Byte bằng bao nhiêu bit?",
  {"A": "4 bit", "B": "8 bit", "C": "16 bit", "D": "1 024 bit"}, "B",
  "1 B = 8 bit; các bội của Byte hơn kém nhau 1 024 lần."),
 (3, "1 MB bằng bao nhiêu KB?",
  {"A": "100 KB", "B": "1 000 KB", "C": "1 024 KB", "D": "1 048 576 KB"}, "C",
  "1 MB = 2¹⁰ KB = 1 024 KB."),
 (4, "Ngoại trừ bit, kể từ Byte thì mỗi đơn vị đo dữ liệu hơn kém nhau bao nhiêu lần?",
  {"A": "10 lần", "B": "100 lần", "C": "1 024 lần", "D": "2 lần"}, "C",
  "Mỗi bậc bằng 2¹⁰ = 1 024 lần: KB → MB → GB → TB → PB."),
 (5, "Phát biểu nào sau đây là SAI khi nói về quan hệ giữa thông tin và dữ liệu?",
  {"A": "Dữ liệu là thông tin đã được đưa vào máy tính", "B": "Thông tin là ý nghĩa của dữ liệu",
   "C": "Thông tin có thể làm thay đổi hành động của con người", "D": "Dữ liệu và thông tin hoàn toàn không liên quan"}, "D",
  "Dữ liệu là nguyên liệu, thông tin là kết quả sau xử lí; hai khái niệm gắn chặt với nhau."),
 (6, "Thông tin được hiểu là gì?",
  {"A": "Các con số lưu trong máy tính", "B": "Những hiểu biết thu được về sự vật, hiện tượng, gắn với nhận thức",
   "C": "Tệp văn bản", "D": "Đường truyền dữ liệu"}, "B",
  "Thông tin là tất cả những gì mang lại hiểu biết cho con người."),
 (7, "Nội dung nào sau đây là dữ liệu?",
  {"A": "Bạn bị sốt cao", "B": "Ngày mai trời sẽ mưa",
   "C": "Dãy số 37; 39; 40; 38; 41 được lưu trong tệp nhietdo.txt", "D": "Lời khuyên nên mang theo ô"}, "C",
  "Dãy số thô là dữ liệu; các kết luận ở A, B, D là thông tin."),
 (8, "Thứ tự đúng của các đơn vị lưu trữ từ nhỏ đến lớn là?",
  {"A": "B, KB, MB, GB, TB", "B": "KB, B, MB, GB, TB", "C": "bit, KB, B, MB, GB", "D": "B, MB, KB, GB, TB"}, "A",
  "bit → B → KB → MB → GB → TB → PB."),
 (9, "Thiết bị nào sau đây là thiết bị thông minh?",
  {"A": "Đồng hồ lịch vạn niên", "B": "Cân cơ học",
   "C": "Đồng hồ kết nối với điện thoại qua bluetooth", "D": "Ổ cắm điện thông thường"}, "C",
  "Có kết nối không dây và xử lí dữ liệu tự chủ (đo nhịp tim, nhận thông báo)."),
 (10, "Thiết bị nào KHÔNG phải là thiết bị thông minh?",
  {"A": "Điện thoại thông minh", "B": "Tivi thông minh", "C": "Robot hút bụi", "D": "Máy ảnh cơ học dùng phim"}, "D",
  "Máy ảnh cơ học không có bộ xử lí số và không kết nối mạng."),
 (11, "Đặc điểm cốt lõi để nhận biết một thiết bị thông minh là gì?",
  {"A": "Có vỏ kim loại", "B": "Hoạt động tự chủ nhờ phần mềm và có khả năng kết nối, trao đổi dữ liệu",
   "C": "Dùng điện 220 V", "D": "Có màn hình màu"}, "B",
  "Tự chủ + kết nối + xử lí/truyền dữ liệu là ba dấu hiệu nhận biết."),
 (12, "Đâu KHÔNG phải là đóng góp cơ bản của tin học đối với xã hội?",
  {"A": "Quản lí nghiệp vụ nhanh, chính xác", "B": "Tự động hoá sản xuất",
   "C": "Giải quyết bài toán khoa học – kĩ thuật", "D": "Chữa khỏi mọi bệnh tật cho con người"}, "D",
  "Tin học hỗ trợ y tế nhưng không thể «chữa khỏi mọi bệnh tật»."),
 (13, "FORTRAN (1957) được biết đến là gì?",
  {"A": "Hệ điều hành đầu tiên", "B": "Ngôn ngữ lập trình bậc cao đầu tiên",
   "C": "Máy tính cá nhân đầu tiên", "D": "Giao thức mạng đầu tiên"}, "B",
  "FORTRAN mở đường cho các ngôn ngữ bậc cao như C, Pascal, Java, Python."),
 (14, "Hệ điều hành OS/360 (1964) có ý nghĩa gì?",
  {"A": "Đặt nền móng cho hệ điều hành hiện đại", "B": "Là ngôn ngữ lập trình đầu tiên",
   "C": "Là mạng máy tính đầu tiên", "D": "Là điện thoại thông minh đầu tiên"}, "A",
  "OS/360 trên dòng máy IBM/360 đưa ra hầu hết nguyên lí của hệ điều hành hiện đại."),
 (15, "Bộ giao thức TCP/IP được thiết lập vào năm nào, tạo nền tảng cho Internet?",
  {"A": "1957", "B": "1964", "C": "1983", "D": "2007"}, "C",
  "TCP/IP (1983) cùng World Wide Web (1989–1992) giúp Internet phổ cập."),
 (16, "Công nghệ nào KHÔNG thuộc nền tảng của cuộc cách mạng công nghiệp 4.0?",
  {"A": "Trí tuệ nhân tạo AI", "B": "Internet vạn vật IoT", "C": "Điện toán đám mây", "D": "Động cơ hơi nước"}, "D",
  "Động cơ hơi nước thuộc CMCN 1.0; CMCN 4.0 gồm AI, IoT, Cloud, Big Data."),
 (17, "Cách tắt máy tính đúng cách là gì?",
  {"A": "Rút dây nguồn ngay lập tức", "B": "Dùng lệnh Shut down trong hệ điều hành",
   "C": "Nhấn giữ nút nguồn 10 giây mỗi lần", "D": "Để máy tự hết pin"}, "B",
  "Shut down giúp hệ điều hành lưu dữ liệu, tránh hỏng tệp hệ thống."),
 (18, "Phần mở rộng nào sau đây thường dùng cho tệp văn bản soạn thảo?",
  {"A": ".docx", "B": ".mp3", "C": ".jpg", "D": ".mp4"}, "A",
  ".docx (Word), .xlsx (Excel), .pptx (PowerPoint), .pdf (PDF), .jpg (ảnh), .mp3 (nhạc)."),
 (19, "Mạng LAN là mạng có đặc điểm gì?",
  {"A": "Phạm vi toàn cầu", "B": "Phạm vi nhỏ như gia đình, trường học, cơ quan",
   "C": "Không có chủ sở hữu", "D": "Chỉ dùng cho điện thoại"}, "B",
  "LAN (Local Area Network) là mạng cục bộ, phạm vi địa lí nhỏ."),
 (20, "Internet được hiểu là gì?",
  {"A": "Mạng cục bộ trong một phòng", "B": "Mạng diện rộng có quy mô toàn cầu, kết nối các mạng LAN",
   "C": "Một phần mềm duyệt web", "D": "Thiết bị định tuyến"}, "B",
  "Internet là mạng của các mạng, quy mô toàn cầu."),
 (21, "Ai là chủ sở hữu của mạng Internet?",
  {"A": "Microsoft", "B": "IBM", "C": "Không ai sở hữu; chỉ có tổ chức điều phối tài nguyên và tiêu chuẩn", "D": "Google"}, "C",
  "Internet không thuộc sở hữu của riêng cá nhân hay tổ chức nào."),
 (22, "Thiết bị nào dùng để kết nối các mạng LAN với Internet?",
  {"A": "Bàn phím", "B": "Router (bộ định tuyến)", "C": "Máy in", "D": "Webcam"}, "B",
  "Router chuyển gói dữ liệu ra cổng Internet khi địa chỉ đích không nằm trong LAN."),
 (23, "Từ IoT được viết đầy đủ là gì?",
  {"A": "Internet of Teacher", "B": "Intel of Things", "C": "Internet of Things", "D": "Internet of Technology"}, "C",
  "IoT = Internet of Things = Internet vạn vật / kết nối vạn vật."),
 (24, "Điện toán đám mây có bao nhiêu loại dịch vụ cơ bản?",
  {"A": "1", "B": "2", "C": "3", "D": "4"}, "C",
  "Ba loại: SaaS (phần mềm), PaaS (nền tảng), IaaS (hạ tầng)."),
 (25, "Gmail, Google Docs và Zoom là ví dụ của loại dịch vụ đám mây nào?",
  {"A": "SaaS", "B": "PaaS", "C": "IaaS", "D": "Không phải đám mây"}, "A",
  "SaaS cho thuê phần mềm ứng dụng chạy trên Internet, không cần cài đặt."),
 (26, "Google Drive và Dropbox là ví dụ điển hình của loại dịch vụ nào?",
  {"A": "SaaS", "B": "PaaS", "C": "IaaS (lưu trữ/hạ tầng)", "D": "Mạng LAN"}, "C",
  "Theo SGK Kết nối tri thức, lưu trữ thông tin qua Drive/Dropbox thuộc IaaS."),
 (27, "Hoạt động nào sau đây KHÔNG được coi là dùng dịch vụ điện toán đám mây?",
  {"A": "Soạn văn bản trên Google Docs", "B": "Lưu ảnh lên Google Drive",
   "C": "Đọc tin tức trên một trang báo điện tử công cộng", "D": "Họp trực tuyến bằng Zoom"}, "C",
  "Đọc báo điện tử chỉ là truy cập thông tin công cộng, không thuê tài nguyên phần mềm/phần cứng."),
 (28, "Ứng dụng nào sau đây là ví dụ điển hình của IoT?",
  {"A": "Viết tay vào vở", "B": "Thu phí không dừng bằng thẻ RFID trên cao tốc",
   "C": "Đọc sách giấy trong thư viện", "D": "Gõ văn bản bằng máy chữ cơ khí"}, "B",
  "Thẻ RFID + cảm biến + mạng + xử lí tự động tạo thành hệ thống IoT."),
 (29, "Phần mềm độc hại (malware) là gì?",
  {"A": "Phần mềm được viết với ý đồ xấu, gây hại cho người dùng, thiết bị hoặc dữ liệu",
   "B": "Phần mềm miễn phí", "C": "Phần mềm hệ điều hành", "D": "Trình duyệt web"}, "A",
  "Malware gồm virus, worm, trojan, spyware, ransomware…"),
 (30, "Điểm khác biệt cơ bản giữa virus và worm là gì?",
  {"A": "Virus là chương trình hoàn chỉnh, worm thì không",
   "B": "Virus chỉ là đoạn mã phải gắn vào chương trình khác; worm là chương trình hoàn chỉnh tự lan qua mạng",
   "C": "Worm không gây hại", "D": "Virus chỉ tồn tại trên điện thoại"}, "B",
  "Virus cần «vật chủ»; worm tự phát tán qua mạng, thường lợi dụng lỗ hổng hệ điều hành."),
]
TN_BANK += [
 (31, "Trojan (phần mềm nội gián) chủ yếu gây tác hại gì?",
  {"A": "Tự nhân bản để lây lan nhanh nhất", "B": "Ăn cắp thông tin và chiếm quyền sử dụng máy tính",
   "C": "Chỉ làm chậm màn hình", "D": "Tăng dung lượng ổ cứng"}, "B",
  "Trojan ít chú trọng lây lan; các dạng của nó là spyware, keylogger, backdoor, rootkit."),
 (32, "WannaCry (2017) là ví dụ về loại mã độc nào?",
  {"A": "Adware quảng cáo", "B": "Sâu/worm mã hoá dữ liệu để tống tiền (ransomware)",
   "C": "Trình duyệt web", "D": "Phần mềm diệt virus"}, "B",
  "WannaCry lây qua lỗ hổng Windows, mã hoá toàn bộ dữ liệu và đòi tiền chuộc."),
 (33, "Công cụ nào được tích hợp sẵn trong Windows 10 để chống virus?",
  {"A": "Microsoft Word", "B": "Windows Defender (Windows Security)",
   "C": "Paint", "D": "Notepad"}, "B",
  "Windows Defender chạy ngầm, tự cập nhật mẫu virus qua Windows Update."),
 (34, "Chế độ Quick scan của Windows Defender có ý nghĩa gì?",
  {"A": "Quét toàn bộ ổ đĩa", "B": "Quét nhanh các thư mục có nguy cơ cao, nơi virus thường lây nhiễm",
   "C": "Chỉ quét một thư mục do người dùng chọn", "D": "Quét khi máy đã tắt"}, "B",
  "Full scan quét mọi ổ đĩa; Custom scan quét thư mục tự chọn; Offline scan xử lí mã độc khó gỡ."),
 (35, "Muốn quét virus cho đúng một thư mục vừa tải về, em chọn cách nào nhanh nhất?",
  {"A": "Cài lại Windows", "B": "Nháy chuột phải vào thư mục → Scan with Microsoft Defender",
   "C": "Đổi tên thư mục", "D": "Tắt mạng Internet"}, "B",
  "Cách này dùng trực tiếp chức năng quét của Defender mà không cần mở cửa sổ chính."),
 (36, "Nguy cơ nào sau đây KHÔNG phải là nguy cơ khi tham gia Internet thiếu hiểu biết?",
  {"A": "Tin giả", "B": "Lừa đảo trên mạng", "C": "Lộ thông tin cá nhân",
   "D": "Được học thêm kiến thức từ bài giảng điện tử"}, "D",
  "Học bài giảng điện tử là lợi ích; các phương án A, B, C là nguy cơ."),
 (37, "Khi bị bắt nạt trên mạng, việc nên làm TRƯỚC TIÊN là gì?",
  {"A": "Đáp trả gay gắt để «đòi lại thể diện»", "B": "Xoá hết tin nhắn cho đỡ phiền",
   "C": "Không tranh luận, lưu giữ bằng chứng và chia sẻ ngay với bố mẹ, thầy cô",
   "D": "Im lặng một mình chịu đựng"}, "C",
  "Lưu bằng chứng + báo người lớn là hai việc quan trọng nhất; nếu nghiêm trọng thì báo công an."),
 (38, "Mật khẩu nào sau đây là mạnh nhất?",
  {"A": "123456", "B": "ngaysinh0910", "C": "Tin@Hoc10#2026", "D": "password"}, "C",
  "Mật khẩu mạnh: dài, gồm chữ hoa, chữ thường, số và kí hiệu; không chứa thông tin cá nhân."),
 (39, "Khi nhận được tin nhắn yêu cầu cung cấp mã OTP «để xác minh tài khoản», em nên làm gì?",
  {"A": "Gửi ngay mã OTP", "B": "Không cung cấp cho ai; kiểm tra lại bằng cách liên hệ trực tiếp với nhà cung cấp",
   "C": "Đăng mã OTP lên mạng xã hội", "D": "Gửi kèm cả mật khẩu để tiện"}, "B",
  "OTP là lớp bảo vệ cuối cùng; kẻ lừa đảo thường mạo danh ngân hàng để chiếm đoạt mã này."),
 (40, "Học liệu mở (OER) có đặc điểm gì?",
  {"A": "Phải trả phí cao mới được đọc", "B": "Chỉ dùng được một lần",
   "C": "Tài nguyên giáo dục miễn phí, được phép sử dụng, chỉnh sửa, chia sẻ hợp pháp theo giấy phép mở",
   "D": "Luôn vi phạm bản quyền"}, "C",
  "OER thường dùng giấy phép Creative Commons; vẫn phải ghi nguồn theo điều kiện giấy phép."),
 (41, "Kí hiệu © trên sản phẩm có ý nghĩa gì?",
  {"A": "Sản phẩm miễn phí hoàn toàn", "B": "Sản phẩm đã được bảo hộ bản quyền, cấm sử dụng khi chưa có phép",
   "C": "Sản phẩm hết hạn sử dụng", "D": "Sản phẩm do Nhà nước phát hành"}, "B",
  "© (Copyrighted) tuyên bố quyền tác giả; cần xin phép chủ sở hữu trước khi khai thác."),
 (42, "Quyền tác giả là gì?",
  {"A": "Quyền mua bán thiết bị", "B": "Quyền của tác giả đối với sáng tạo tinh thần, văn hoá của mình",
   "C": "Quyền dùng Internet miễn phí", "D": "Quyền đặt tên máy tính"}, "B",
  "Các sản phẩm số (bài viết, ảnh, video, phần mềm, website) cũng được bảo hộ."),
 (43, "Luật Công nghệ thông tin Việt Nam được ban hành năm nào?",
  {"A": "2005", "B": "2006", "C": "2013", "D": "2018"}, "B",
  "Luật CNTT số 67/2006/QH11; Điều 12 quy định các hành vi bị cấm."),
 (44, "Điều 12 của Luật Công nghệ thông tin quy định về nội dung gì?",
  {"A": "Các hành vi bị cấm trong hoạt động CNTT, trong đó có thông tin số xuyên tạc, vu khống, xúc phạm danh dự",
   "B": "Giá cước Internet", "C": "Cách đặt mật khẩu", "D": "Tiêu chuẩn bàn phím"}, "A",
  "Khoản 2 Điều 12 là nội dung trọng tâm của bài học về tuân thủ pháp luật."),
 (45, "Luật An ninh mạng số 24/2018/QH14 có hiệu lực từ khi nào?",
  {"A": "1/1/2007", "B": "1/1/2013", "C": "1/1/2019", "D": "1/6/2021"}, "C",
  "Luật được Quốc hội thông tháng 6/2018, có hiệu lực ngày 1/1/2019."),
 (46, "Theo điểm d khoản 1 Điều 8 Luật An ninh mạng, hành vi nào bị nghiêm cấm?",
  {"A": "Đăng thông tin sai sự thật gây hoang mang trong nhân dân", "B": "Đọc báo điện tử",
   "C": "Gửi email cho bạn bè", "D": "Học trực tuyến"}, "A",
  "Đây là căn cứ xử lí các trường hợp phát tán tin giả trên mạng xã hội."),
 (47, "Nghị định 72/2013/NĐ-CP quy định về vấn đề gì?",
  {"A": "Quản lí, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng",
   "B": "Giá bán máy tính", "C": "Bản quyền âm nhạc", "D": "An toàn giao thông"}, "A",
  "Nghị định 72/2013/NĐ-CP (sửa đổi bởi Nghị định 27/2018/NĐ-CP) quản lí trang thông tin điện tử, mạng xã hội."),
 (48, "Nghị định 131/2013/NĐ-CP quy định về nội dung nào?",
  {"A": "Xử phạt vi phạm hành chính về quyền tác giả, quyền liên quan",
   "B": "Cấp phép Internet", "C": "Đặt tên miền .vn", "D": "Bảo vệ trẻ em trên mạng"}, "A",
  "Phạt 5–10 triệu đồng với hành vi công bố tác phẩm trái phép; 15–35 triệu với hành vi sao chép trái phép."),
 (49, "Theo khoản 1 Điều 101 Nghị định 15/2020/NĐ-CP, chia sẻ thông tin giả mạo, sai sự thật trên mạng xã hội bị phạt bao nhiêu?",
  {"A": "1–2 triệu đồng", "B": "5–10 triệu đồng", "C": "10–20 triệu đồng", "D": "100–200 triệu đồng"}, "C",
  "Ngoài phạt tiền còn buộc gỡ bỏ thông tin vi phạm."),
 (50, "Điều 25 Luật Sở hữu trí tuệ quy định điều gì?",
  {"A": "Các hành vi xâm phạm quyền tác giả", "B": "Các trường hợp sử dụng tác phẩm đã công bố không phải xin phép, không phải trả nhuận bút",
   "C": "Thời hạn bảo hộ bằng sáng chế", "D": "Thủ tục đăng kí tên miền"}, "B",
  "Ví dụ: trích dẫn hợp lí tác phẩm, không làm sai ý tác giả, để bình luận hoặc minh hoạ."),
 (51, "Điều 28 Luật Sở hữu trí tuệ liệt kê điều gì?",
  {"A": "Các hành vi xâm phạm quyền tác giả", "B": "Các loại thiết bị số",
   "C": "Các đơn vị lưu trữ dữ liệu", "D": "Các dịch vụ đám mây"}, "A",
  "Các khoản 7, 8, 10 Điều 28 thường được dùng để xét hành vi sao chép, đăng tải trái phép."),
 (52, "Hành vi nào sau đây KHÔNG vi phạm bản quyền?",
  {"A": "Chép đĩa cài phần mềm bản quyền cho bạn", "B": "Tải bài hát rồi đăng lại lên kênh của mình",
   "C": "Trích dẫn một đoạn ngắn, ghi rõ tên tác giả và nguồn, không làm sai ý tác giả", "D": "Dùng chung tài khoản khoá học trực tuyến"}, "C",
  "Trích dẫn hợp lí thuộc trường hợp ngoại lệ tại Điều 25 Luật SHTT."),
 (53, "Hành vi nào sau đây là vi phạm bản quyền thông tin và sản phẩm số?",
  {"A": "Mua phần mềm bản quyền và cài đúng số máy cho phép", "B": "Tự ý đăng lại toàn bộ bài viết của người khác lên website công ty",
   "C": "Dùng ảnh Creative Commons và ghi nguồn đúng quy định", "D": "Viết bài mới bằng chính ý tưởng của mình"}, "B",
  "Sao chép, phân phối, truyền đạt tác phẩm không có phép của chủ sở hữu là xâm phạm quyền tác giả."),
 (54, "Theo Điều 18 Nghị định 131/2013/NĐ-CP, hành vi sao chép tác phẩm trái phép bị phạt bao nhiêu?",
  {"A": "1–3 triệu đồng", "B": "5–10 triệu đồng", "C": "10–15 triệu đồng", "D": "15–35 triệu đồng"}, "D",
  "Đây là mức phạt thường được hỏi trong các bài tập SGK."),
 (55, "Theo Điều 11 Nghị định 131/2013/NĐ-CP, hành vi công bố tác phẩm trái phép bị phạt bao nhiêu?",
  {"A": "5–10 triệu đồng", "B": "15–35 triệu đồng", "C": "50–100 triệu đồng", "D": "Không bị phạt"}, "A",
  "Phân biệt: công bố trái phép 5–10 triệu; sao chép trái phép 15–35 triệu đồng."),
 (56, "Việc bấm Like, Share vào một bài viết có thông tin sai trái có thể dẫn đến hệ quả gì?",
  {"A": "Không có hệ quả gì", "B": "Tiếp tay lan truyền thông tin sai, bài viết tiếp cận nhiều người hơn và người dùng có thể bị xử phạt",
   "C": "Tự động xoá bài viết", "D": "Được thưởng điểm"}, "B",
  "Theo SGK, hành vi này có thể bị xử phạt theo khoản 1 Điều 101 Nghị định 15/2020/NĐ-CP."),
 (57, "Hành vi nào sau đây KHÔNG vi phạm pháp luật khi chia sẻ thông tin trên mạng?",
  {"A": "Chia sẻ thông tin giả mạo", "B": "Chia sẻ bí mật nhà nước",
   "C": "Chia sẻ thông tin đúng sự thật, đã kiểm chứng, ghi rõ nguồn hợp pháp", "D": "Đăng thông tin cá nhân của người khác không có phép"}, "C",
  "Muốn chia sẻ hợp pháp cần kiểm chứng nội dung và tôn trọng quyền riêng tư, bản quyền."),
 (58, "Bộ Quy tắc ứng xử trên mạng xã hội được ban hành theo văn bản nào?",
  {"A": "Quyết định 874/QĐ-BTTTT ngày 17/6/2021", "B": "Luật CNTT 2006",
   "C": "Nghị định 131/2013/NĐ-CP", "D": "Luật SHTT 2005"}, "A",
  "Bộ quy tắc khuyến khích ứng xử văn minh, không đăng tin giả, không phát ngôn thù ghét."),
 (59, "Hành vi nào thuộc nhóm vấn đề VĂN HOÁ trong môi trường số?",
  {"A": "Sao chép phần mềm có bản quyền", "B": "Dùng ngôn từ thô tục, xúc phạm danh dự người khác trong bình luận",
   "C": "Đánh cắp mật khẩu", "D": "Phát tán mã độc"}, "B",
  "A, C, D thiên về vi phạm pháp luật; B là biểu hiện thiếu văn hoá ứng xử."),
 (60, "Một người đăng tin bịa đặt «công ty X phá sản» làm công ty X mất đơn hàng. Hành vi này vi phạm văn bản nào TRƯỚC HẾT?",
  {"A": "Điểm d khoản 1 Điều 8 Luật An ninh mạng 2018 và khoản 1 Điều 101 Nghị định 15/2020/NĐ-CP",
   "B": "Luật Giao dịch điện tử 2005", "C": "Quy chuẩn bàn phím", "D": "Không vi phạm văn bản nào"}, "A",
  "Tin sai sự thật gây thiệt hại cho tổ chức là hành vi bị cấm, bị xử phạt và phải bồi thường."),
]

DS_BANK = [
 (1, "Đọc đoạn thông tin sau và đánh giá các nhận định: «Máy tính tiếp nhận dữ liệu, xử lí và đưa ra kết quả. Dữ liệu là thông tin đã được đưa vào máy tính; 1 MB = 1 024 KB.»",
  [("a", "Quá trình xử lí thông tin của máy tính gồm 3 bước: tiếp nhận, xử lí, đưa ra kết quả."),
   ("b", "Thông tin là dữ liệu đã được đưa vào máy tính."),
   ("c", "1 MB = 1 000 KB."),
   ("d", "Kết quả xử lí có thể được lưu thành tệp và truyền đi qua mạng.")], "DSSD",
  "a đúng; b sai (ngược lại: dữ liệu là thông tin đã đưa vào máy); c sai (1 MB = 1 024 KB); d đúng."),
 (2, "Đọc đoạn thông tin và đánh giá các nhận định: «Thiết bị thông minh hoạt động tự chủ nhờ phần mềm, có thể kết nối không dây. FORTRAN (1957), OS/360 (1964), TCP/IP (1983) và WWW (1992) là các mốc phát triển của tin học.»",
  [("a", "Đồng hồ kết nối bluetooth với điện thoại là một thiết bị thông minh."),
   ("b", "Máy tính xách tay không phải là thiết bị thông minh."),
   ("c", "Thiết bị thông minh là một hệ thống xử lí thông tin gồm đầu vào, xử lí, lưu trữ và đầu ra."),
   ("d", "Cách mạng công nghiệp 4.0 gắn liền với AI, IoT, điện toán đám mây và dữ liệu lớn.")], "DSDĐ",
  "a đúng; b sai (laptop có hệ điều hành, phần mềm và kết nối mạng); c, d đúng."),
 (3, "Đọc đoạn thông tin và đánh giá các nhận định: «LAN là mạng cục bộ; Internet là mạng toàn cầu. Điện toán đám mây cung cấp SaaS, PaaS, IaaS qua Internet. IoT kết nối thiết bị thông minh để tự động thu thập, trao đổi, xử lí dữ liệu.»",
  [("a", "Mạng LAN có phạm vi nhỏ và thuộc sở hữu của một cá nhân hoặc tổ chức."),
   ("b", "Internet thuộc sở hữu của công ty Google."),
   ("c", "Google Drive và Dropbox là ví dụ về dịch vụ lưu trữ trên đám mây."),
   ("d", "Thu phí không dừng bằng thẻ RFID là một ứng dụng của IoT.")], "DSDĐ",
  "a đúng; b sai (Internet không có chủ sở hữu riêng); c, d đúng."),
 (4, "Đọc đoạn thông tin và đánh giá các nhận định: «Virus phải gắn vào chương trình khác; worm tự lan qua mạng; trojan chuyên ăn cắp thông tin. Windows Defender có các chế độ Quick scan, Full scan, Custom scan.»",
  [("a", "Virus là một chương trình hoàn chỉnh, có thể tự chạy độc lập."),
   ("b", "Worm thường lợi dụng lỗ hổng hệ điều hành hoặc lừa người dùng mở liên kết."),
   ("c", "Khi bị bắt nạt trên mạng, nên lưu bằng chứng và nói với bố mẹ, thầy cô."),
   ("d", "Nên dùng cùng một mật khẩu dễ nhớ cho mọi tài khoản.")], "SĐĐS",
  "a sai (virus chỉ là đoạn mã); b, c đúng; d sai (mỗi tài khoản một mật khẩu mạnh, khác nhau)."),
 (5, "Đọc đoạn thông tin và đánh giá các nhận định: «Luật CNTT 2006, Luật An ninh mạng 2018, Nghị định 72/2013/NĐ-CP và Luật SHTT là các văn bản quan trọng điều chỉnh hoạt động trong môi trường số.»",
  [("a", "Kí hiệu © cho biết sản phẩm đã được bảo hộ bản quyền."),
   ("b", "Tự ý tải nhạc và đăng lại lên kênh cá nhân để lấy view là hành vi hợp pháp."),
   ("c", "Chia sẻ thông tin sai sự thật trên mạng xã hội có thể bị xử phạt 10–20 triệu đồng."),
   ("d", "Cần kiểm chứng nguồn tin và ghi rõ nguồn tác giả khi sử dụng lại nội dung của người khác.")], "DSDĐ",
  "a đúng; b sai (vi phạm bản quyền); c đúng (Điều 101 Nghị định 15/2020); d đúng."),
 (6, "Tình huống: «Công ty A đăng bài viết và video minh hoạ lấy từ trang web của nhà sản xuất game nước ngoài mà không xin phép. Cùng thời điểm, một tài khoản mạng xã hội chia sẻ tin đồn sai sự thật về công ty A.»",
  [("a", "Công ty A đã vi phạm Luật Sở hữu trí tuệ (Điều 28) về quyền tác giả."),
   ("b", "Công ty A chỉ cần ghi tên trang web là dùng được tác phẩm mà không cần xin phép."),
   ("c", "Người đăng tin đồn sai sự thật có thể bị xử phạt theo Nghị định 15/2020/NĐ-CP."),
   ("d", "Việc xác định tính hợp pháp cần mô tả hành vi, đối chiếu văn bản luật, kết luận và nêu chế tài.")], "DSDĐ",
  "a đúng; b sai (ghi nguồn không thay thế được sự cho phép nếu dùng toàn bộ tác phẩm); c, d đúng."),
 (7, "Đọc đoạn thông tin và đánh giá các nhận định: «Một thẻ nhớ 256 GB có thể chứa 2 000 cuốn sách số hoá, mỗi cuốn 50 MB.»",
  [("a", "Tổng dung lượng 2 000 cuốn sách là 100 000 MB."),
   ("b", "100 000 MB ≈ 97,66 GB."),
   ("c", "Thẻ 256 GB không đủ chứa 2 000 cuốn sách nói trên."),
   ("d", "Lưu trữ bằng thiết bị số cho phép sao chép dữ liệu không bị suy giảm chất lượng.")], "ĐĐSĐ",
  "a đúng (2 000 × 50); b đúng (100 000 : 1 024 ≈ 97,66); c sai (256 GB > 97,66 GB, thừa chỗ); d đúng."),
 (8, "Đọc đoạn thông tin và đánh giá các nhận định: «Học sinh dùng Google Translate để dịch một đoạn văn, sau đó tải bài giảng từ một nguồn học liệu mở và đăng lại lên nhóm học tập.»",
  [("a", "Bản dịch máy cần được rà soát lại trước khi dùng chính thức."),
   ("b", "Học liệu mở cho phép dùng, sửa, chia sẻ hợp pháp nhưng vẫn cần đọc điều kiện giấy phép và ghi nguồn."),
   ("c", "Nhận dạng tiếng nói là một chức năng xử lí thông tin trên thiết bị số."),
   ("d", "Vì là học liệu mở nên không bao giờ cần ghi tên tác giả.")], "ĐĐĐS",
  "a, b, c đúng; d sai (đa số giấy phép CC vẫn yêu cầu ghi nguồn)."),
]

TL_BANK = [
 (1, "Em hãy nêu các đơn vị đo lượng thông tin theo thứ tự tăng dần và cho biết quy tắc chuyển đổi giữa chúng. Lấy ví dụ minh hoạ.",
  "Thứ tự: bit → B → KB → MB → GB → TB → PB. 1 B = 8 bit; kể từ Byte, mỗi đơn vị hơn kém 2¹⁰ = 1 024 lần: 1 KB = 1 024 B, 1 MB = 1 024 KB, 1 GB = 1 024 MB, 1 TB = 1 024 GB, 1 PB = 1 024 TB. Đổi lớn sang nhỏ thì nhân 1 024, đổi nhỏ sang lớn thì chia 1 024. Ví dụ: 3 MB = 3 × 1 024 = 3 072 KB; 2 GB = 2 × 1 024 × 1 024 = 2 097 152 KB; 3 072 B = 3 KB."),
 (2, "Một thư viện số hoá 2 000 cuốn sách, mỗi cuốn 50 MB. Ổ cứng 256 GB có chứa được không? Hãy tính toán cụ thể.",
  "Tổng dung lượng = 2 000 × 50 = 100 000 MB. Đổi sang GB: 100 000 : 1 024 ≈ 97,66 GB. So sánh: 97,66 GB < 256 GB → ổ cứng chứa được toàn bộ thư viện, còn dư khoảng 158,34 GB. (Có thể giải theo hướng đổi 256 GB = 262 144 MB > 100 000 MB.)"),
 (3, "Em hãy mô tả quy trình xử lí và truyền thông tin bằng thiết bị số, lấy ví dụ cụ thể một bức ảnh được gửi từ điện thoại này sang điện thoại khác.",
  "Gồm 3 bước: (1) Tiếp nhận dữ liệu – camera thu ánh sáng, cảm biến chuyển thành dữ liệu số, lưu thành tệp ảnh; (2) Xử lí dữ liệu – phần mềm nén, gắn nhãn thời gian/địa điểm, lưu vào bộ nhớ; (3) Đưa ra kết quả và truyền – màn hình hiển thị ảnh; khi bấm Gửi, điện thoại dùng wifi/4G/5G, giao thức TCP/IP truyền tệp qua Internet đến máy chủ ứng dụng rồi tới máy nhận, nơi ảnh được giải nén và hiển thị. Ngoài ra có thể dùng chức năng dịch tự động để dịch chú thích của bức ảnh sang tiếng Việt trước khi gửi."),
 (4, "Em hãy kể tên ít nhất bốn ứng dụng của Tin học đối với giáo dục và bốn ứng dụng trong giao tiếp cộng đồng.",
  "Giáo dục: (1) tra cứu tài liệu, bài giảng điện tử trên Internet; (2) học trực tuyến qua Zoom/Google Meet và hệ thống quản lí học tập; (3) dùng phần mềm văn phòng soạn bài, làm bài trình chiếu; (4) dùng ứng dụng học ngoại ngữ, luyện tập trắc nghiệm, thư viện số và học liệu mở; (5) học lập trình qua môi trường trực tuyến. Giao tiếp cộng đồng: (1) thư điện tử; (2) mạng xã hội Facebook, Zalo; (3) diễn đàn, nhóm chat, nhóm học tập; (4) gọi điện/video trực tuyến; (5) bình luận, chia sẻ và phản hồi tức thời trên báo điện tử."),
 (5, "Theo em, vì sao thiết bị thông minh lại giữ vai trò chủ chốt trong cuộc cách mạng công nghiệp 4.0? Hãy giải thích và nêu ví dụ.",
  "CMCN 4.0 dựa trên công nghệ số với AI, IoT, điện toán đám mây, dữ liệu lớn. Thiết bị thông minh có cảm biến và phần mềm nên thu thập dữ liệu tự động, liên tục, tức thời trên diện rộng, truyền qua mạng về trung tâm để AI phân tích và tự động điều khiển lại thiết bị – tạo thành hệ thống sản xuất thông minh, làm mờ ranh giới thế giới thực và thế giới ảo. Ví dụ: camera giao thông thông minh nhận diện biển số và tự động ghi nhận vi phạm; công tơ điện tử gửi số liệu tiêu thụ về trung tâm để dự báo phụ tải; robot trong nhà máy tự phối hợp qua mạng. Nhờ đó năng suất tăng, chi phí giảm, quyết định chính xác hơn, thúc đẩy kinh tế tri thức."),
 (6, "Em hãy trình bày các thao tác cơ bản để quản lí tệp dữ liệu trên máy tính và nêu lưu ý khi sử dụng phần mềm ứng dụng cài sẵn.",
  "Các thao tác: tạo thư mục; tạo tệp mới; đổi tên; sao chép – dán; di chuyển; xoá; nén/giải nén; tìm kiếm theo tên, ngày, loại tệp; mở tệp bằng đúng phần mềm (.docx bằng Word, .xlsx bằng Excel, .pdf bằng trình đọc PDF); lưu (Ctrl+S) và «Lưu thành»; chia sẻ qua email/đám mây. Lưu ý: đặt tên tệp ngắn gọn, không dấu, có phần mở rộng đúng; sắp xếp theo thư mục chủ đề; không lưu mọi thứ trên Desktop; chỉ cài ứng dụng từ nguồn chính thức, đọc kĩ quyền truy cập; sao lưu định kì và quét virus tệp tải về."),
 (7, "Hãy trình bày những thay đổi về phương thức học tập và làm việc khi mạng máy tính được sử dụng phổ biến.",
  "Học tập: nguồn học liệu khổng lồ trên Internet, bài giảng điện tử, thư viện số và học liệu mở; học trực tuyến, học từ xa, học mọi lúc mọi nơi; công cụ cộng tác giúp thảo luận nhóm, nộp bài, nhận phản hồi nhanh; học suốt đời trở thành hiện thực. Làm việc: họp trực tuyến, làm việc từ xa, chia sẻ và cộng tác trên tài liệu đám mây; quản lí dự án, kí hợp đồng điện tử, thanh toán và thủ tục hành chính trực tuyến; dữ liệu được cập nhật tức thời giúp ra quyết định nhanh. Bên cạnh đó cần chú ý tin giả, bảo mật thông tin và cân bằng thời gian trực tuyến."),
 (8, "Em hãy nêu hai ví dụ về IoT, phân tích lợi ích và phát biểu ý kiến cá nhân về những lưu ý khi triển khai IoT.",
  "Ví dụ 1: thu phí không dừng – thẻ RFID được đọc tự động, dữ liệu gửi về trung tâm trừ phí và mở barie → giảm ùn tắc, không cần nhân viên thu tiền. Ví dụ 2: nhà thông minh – cảm biến nhiệt độ/ánh sáng điều khiển điều hoà, đèn, rèm; chủ nhà điều khiển bằng giọng nói → tiện nghi, tiết kiệm điện, an toàn. Lợi ích chung: thu thập dữ liệu tự động, liên tục, tức thời trên diện rộng; làm việc được trong môi trường nguy hiểm; giảm chi phí nhân công; hỗ trợ quyết định nhanh. Ý kiến cá nhân: IoT rất hữu ích nhưng cần bảo mật thiết bị (đổi mật khẩu mặc định, cập nhật firmware), mã hoá dữ liệu truyền đi, chỉ thu thập dữ liệu cần thiết và tôn trọng quyền riêng tư người dùng, tránh biến nhà thông minh thành công cụ theo dõi."),
 (9, "Em hãy nêu ít nhất sáu cách phòng vệ khi tham gia các hoạt động trên Internet và giải thích ngắn gọn từng cách.",
  "Kiểm chứng nguồn tin trước khi tin/chia sẻ (tránh tin giả). Không tiết lộ thông tin cá nhân, mã OTP, mật khẩu (tránh lừa đảo). Dùng mật khẩu mạnh, riêng cho từng tài khoản và bật xác thực 2 yếu tố (chống chiếm tài khoản). Không mở link/tệp đính kèm lạ, xác minh lại qua điện thoại (chống malware, phishing). Cập nhật hệ điều hành, dùng phần mềm diệt virus, quét tệp trước khi mở (ngăn mã độc). Không tải phần mềm bẻ khoá, chỉ cài từ kho chính thức (tránh trojan). Không kết bạn bừa bãi, ứng xử văn minh (tránh bắt nạt). Sao lưu dữ liệu quan trọng (giảm thiệt hại khi sự cố)."),
 (10, "Em hãy hướng dẫn chi tiết cách quét virus bằng Windows Defender và phân biệt bốn chế độ quét.",
  "Mở Start → gõ «Windows Security» → chọn «Virus & threat protection». Tại đây xem Current threats (nguy cơ gần đây), bấm Quick scan để quét nhanh hoặc vào Scan options → chọn kiểu quét → Scan now → chờ kết quả và xử lí theo khuyến nghị. Bốn chế độ: Quick scan – quét các thư mục virus thường lây nhiễm, nhanh; Full scan – quét tất cả ổ đĩa, lâu hơn; Custom scan – chỉ quét thư mục do người dùng chọn; Windows Defender Offline scan – quét ngoại tuyến, dùng cho mã độc khó gỡ, máy sẽ khởi động lại. Ngoài ra có thể nháy chuột phải vào tệp/thư mục → Scan with Microsoft Defender để quét tại chỗ."),
 (11, "Học liệu mở là gì? Em hãy trình bày quy trình khai thác một nguồn học liệu mở trên Internet để viết bài thuyết trình môn Tin học.",
  "Học liệu mở (OER) là tài nguyên giáo dục được cung cấp miễn phí, cho phép người học sử dụng, chỉnh sửa và chia sẻ lại hợp pháp, thường kèm giấy phép Creative Commons. Quy trình: (1) Xác định chủ đề, ví dụ «IoT là gì»; (2) Tìm kiếm với từ khoá kèm «OER»/«Creative Commons»/«bài giảng điện tử», ưu tiên nguồn uy tín (Khan Academy, MIT OCW, trang ĐH, cổng bài giảng điện tử); (3) Đọc giấy phép để biết có được phép sửa, có phải ghi nguồn, có bị cấm dùng thương mại; (4) Đọc, ghi chép, chọn lọc nội dung và hình ảnh; (5) Đưa vào bài thuyết trình kèm trích dẫn rõ ràng: tên tác giả, tên tài liệu, địa chỉ URL, ngày truy cập; (6) Kiểm tra lại bản quyền trước khi đăng bài lên mạng."),
 (12, "Em hãy lập kế hoạch bảo vệ dữ liệu cá nhân cho tài khoản mạng xã hội và email của mình (ít nhất sáu biện pháp kèm lí do).",
  "Đặt mật khẩu mạnh, khác nhau cho từng tài khoản (tránh lộ hàng loạt nếu một nơi bị lộ). Bật xác thực 2 yếu tố (thêm lớp bảo vệ khi mật khẩu bị lộ). Không chia sẻ mật khẩu, mã OTP (chống lừa đảo mạo danh). Cài chế độ riêng tư, hạn chế đăng ảnh CCCD, số điện thoại, lịch trình (tránh bị thu thập, mạo danh). Kiểm tra và thu hồi quyền ứng dụng không cần thiết (tránh ứng dụng thu thập dữ liệu thừa). Không đăng nhập trên máy công cộng hoặc wifi công cộng không mã hoá; luôn đăng xuất (tránh chiếm quyền). Cập nhật hệ điều hành, dùng phần mềm diệt virus (chống keylogger). Sao lưu và xoá dữ liệu cũ không cần thiết."),
 (13, "Bạn Nam thấy một bài hát đang «hot» trên mạng nên tải về và đăng tải lại lên kênh YouTube của mình. Việc làm của Nam đúng hay sai? Hãy phân tích theo văn bản pháp luật đã học và nêu hậu quả.",
  "Việc làm của Nam là SAI, vi phạm bản quyền. Phân tích: bài hát là tác phẩm được bảo hộ quyền tác giả; Nam tự ý sao chép (tải về), phân phối và truyền đạt tác phẩm tới công chúng qua mạng mà không có sự cho phép của chủ sở hữu, thuộc hành vi xâm phạm quyền tác giả theo Điều 28 Luật Sở hữu trí tuệ 50/2005/QH11 (sửa đổi 2019) và thông tin trên mạng chịu điều chỉnh của Nghị định 72/2013/NĐ-CP. Hậu quả: video bị gỡ, kênh có thể bị hạn chế/tắt kiếm tiền; Nam phải xin lỗi, bồi thường thiệt hại; có thể bị phạt 15–35 triệu đồng theo Nghị định 131/2013/NĐ-CP về hành vi sao chép trái phép; uy tín cá nhân bị ảnh hưởng. Cách đúng: xin phép và trả phí bản quyền, dùng nhạc có giấy phép Creative Commons/nhạc miễn phí bản quyền có ghi nguồn, hoặc tự sáng tác."),
 (14, "Công ty A cố tình đăng thông tin sai sự thật về công ty B, làm công ty B thiệt hại lớn về kinh tế. Hành vi của A có vi phạm pháp luật không? Theo văn bản nào? Cần xử lí thế nào?",
  "Có vi phạm. Căn cứ: điểm d khoản 1 Điều 8 Luật An ninh mạng số 24/2018/QH14 nghiêm cấm đưa thông tin sai sự thật gây hoang mang, xâm hại quyền và lợi ích hợp pháp của tổ chức, cá nhân; khoản 2 Điều 12 Luật Công nghệ thông tin 2006 cấm thông tin số xúc phạm uy tín của tổ chức; Nghị định 72/2013/NĐ-CP quản lí thông tin trên mạng; chế tài theo khoản 1 Điều 101 Nghị định 15/2020/NĐ-CP (phạt 10–20 triệu đồng, buộc gỡ bỏ thông tin). Xử lí: công ty B lưu bằng chứng (ảnh chụp, đường dẫn, thời gian), yêu cầu A gỡ bài và cải chính công khai, gửi đơn đến cơ quan nhà nước có thẩm quyền để xử phạt hành chính; đồng thời có thể khởi kiện dân sự đòi bồi thường thiệt hại doanh thu. Nếu hành vi mang tính vu khống, xúc phạm danh dự nghiêm trọng, có thể bị xem xét trách nhiệm hình sự."),
 (15, "Em hãy trình bày quy trình 4 bước vận dụng Luật và Nghị định để xác định tính hợp pháp của một hành vi trong môi trường số, rồi áp dụng vào tình huống: «Một trang web đăng lại toàn bộ bài viết và video của báo điện tử X mà không xin phép, không ghi nguồn».",
  "Quy trình: (1) Mô tả hành vi (ai làm gì, với tác phẩm/dữ liệu nào, có xin phép không); (2) Đối chiếu văn bản pháp luật (Luật CNTT Điều 12, Luật An ninh mạng Điều 8, Nghị định 72/2013 Điều 5, Luật SHTT Điều 25/28, Nghị định 131/2013, Nghị định 15/2020 Điều 101); (3) Kết luận hợp pháp hay vi phạm; (4) Nêu hậu quả, chế tài và cách xử lí đúng. Áp dụng: bước 1 – trang web sao chép và đăng tải lại trọn vẹn bài viết, video của báo X, không xin phép, không ghi nguồn. Bước 2 – đây là hành vi nhân bản, phân phối, truyền đạt tác phẩm không có phép, vi phạm các khoản 7, 8, 10 Điều 28 Luật Sở hữu trí tuệ; đồng thời là hành vi cung cấp, sử dụng thông tin số trái phép theo Luật CNTT và Nghị định 72/2013. Bước 3 – kết luận hành vi KHÔNG hợp pháp. Bước 4 – hậu quả: bị buộc gỡ bỏ bản sao dưới mọi hình thức điện tử, xin lỗi và bồi thường; phạt hành chính theo Nghị định 131/2013/NĐ-CP (5–10 triệu đồng với công bố trái phép, 15–35 triệu đồng với sao chép trái phép). Cách đúng: xin phép và thoả thuận trả phí bản quyền, hoặc chỉ trích dẫn hợp lí một phần nhỏ kèm ghi rõ tên tác giả, tên báo, địa chỉ nguồn và ngày công bố."),
]

story.append(H1("PHẦN V", "NGÂN HÀNG CÂU HỎI LUYỆN TẬP (CÓ ĐÁP ÁN & GIẢI THÍCH)"))
story.append(P("Phần V gồm <b>60 câu trắc nghiệm 4 lựa chọn</b>, <b>8 câu đúng/sai</b> và <b>15 câu tự luận</b>. "
               "Tất cả đều có đáp án và giải thích ngay bên dưới, được xây dựng bám sát 35 yêu cầu cần đạt ở Phần IV."))
story.append(H2("V.1. 60 câu trắc nghiệm 4 lựa chọn"))
for i, (num, q, opts, ans, ex) in enumerate(TN_BANK):
    story.append(MCQ(str(num), q, opts, ans, ex))
    story.append(Spacer(1, 2.5))
    if i in (19, 39):
        story.append(PageBreak())
story.append(H2("V.2. Bảng đáp án nhanh – 60 câu trắc nghiệm"))
ans_cells = []
for start in range(0, 60, 12):
    row1 = ["Câu"] + [str(n) for n, *_ in TN_BANK[start:start+12]]
    row2 = ["Đáp án"] + [a for _, _, _, a, _ in TN_BANK[start:start+12]]
    ans_cells.append(row1)
    ans_cells.append(row2)
t = Table([[Paragraph(esc(c), ST["cellb"] if r % 2 == 0 else ST["cell"]) for c in row]
           for r, row in enumerate(ans_cells)], colWidths=[52] + [34.4]*12)
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE),
                       ("BACKGROUND", (0, 0), (-1, 0), BGBLUE),
                       ("BACKGROUND", (0, 2), (-1, 2), BGBLUE),
                       ("BACKGROUND", (0, 4), (-1, 4), BGBLUE),
                       ("BACKGROUND", (0, 6), (-1, 6), BGBLUE),
                       ("BACKGROUND", (0, 8), (-1, 8), BGBLUE),
                       ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                       ("TOPPADDING", (0, 0), (-1, -1), 4),
                       ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
story.append(t)
story.append(H2("V.3. 8 câu trắc nghiệm lựa chọn đúng/sai"))
for num, stem, statements, answers, explain in DS_BANK:
    story.append(TFQ("ĐS" + str(num), stem, statements, answers, explain))
    story.append(Spacer(1, 3))
story.append(P("<b>Cách tính điểm câu đúng/sai:</b> mỗi câu 1,0 điểm, gồm 4 ý; đúng hết 4 ý được 1,0 điểm; "
               "đúng 3 ý được 0,75; đúng 2 ý được 0,5; đúng 1 ý được 0,25; sai hết 0 điểm (theo cách chấm phổ biến).", "tinyj"))
story.append(PageBreak())
story.append(H2("V.4. 15 câu tự luận (có đáp án gợi ý chi tiết)"))
for num, q, ans in TL_BANK:
    story.append(QA("TL " + str(num), q, ans, "Tự luận"))
    story.append(Spacer(1, 4))
story.append(PageBreak())

# ==========================================================================
# PHAN VI - DE THI THU (DUNG CAU TRUC MA TRAN)
# ==========================================================================
story.append(H1("PHẦN VI", "ĐỀ THI THỬ KIỂM TRA GIỮA KÌ I (45 PHÚT)"))
story.append(BOX([
    P("<b>Thời gian làm bài: 45 phút.</b> Đề gồm 20 câu trắc nghiệm 4 lựa chọn (mỗi câu 0,25 điểm), "
      "2 câu trắc nghiệm đúng/sai (mỗi câu 1,0 điểm) và 3 câu tự luận (mỗi câu 1,0 điểm). Tổng: 10 điểm.", "note"),
    P("<b>Phân bổ:</b> Nhận biết 40% · Thông hiểu 30% · Vận dụng 20% · Vận dụng cao 10%. "
      "Chủ đề A 40% · Chủ đề B 40% · Chủ đề D 20%.", "note"),
], bg=BGAMB, border=AMBER, leftbar=AMBER))

EXAM_TN = [
 (1, "Trong máy tính, đơn vị nhỏ nhất để đo lượng thông tin là", {"A": "Byte", "B": "Bit", "C": "Kilobyte", "D": "Megabyte"}, "B"),
 (2, "1 GB bằng bao nhiêu MB?", {"A": "100", "B": "1 000", "C": "1 024", "D": "1 048 576"}, "C"),
 (3, "Phát biểu nào đúng về dữ liệu và thông tin?", {"A": "Dữ liệu là kết quả xử lí của thông tin", "B": "Dữ liệu là thông tin đã được đưa vào máy tính để xử lí", "C": "Thông tin và dữ liệu là một", "D": "Chỉ có thông tin, không có dữ liệu"}, "B"),
 (4, "Ưu việt nào KHÔNG phải của việc lưu trữ bằng thiết bị số?", {"A": "Dung lượng lớn trong kích thước nhỏ gọn", "B": "Sao chép nhiều lần không giảm chất lượng", "C": "Tự động biến mất sau một năm nếu không đọc lại", "D": "Truyền đi xa nhanh chóng qua mạng"}, "C"),
 (5, "Thiết bị nào sau đây KHÔNG phải thiết bị thông minh?", {"A": "Đồng hồ lịch vạn niên chạy pin", "B": "Điện thoại thông minh", "C": "Tivi thông minh", "D": "Robot hút bụi"}, "A"),
 (6, "Ngôn ngữ lập trình bậc cao đầu tiên (1957) là", {"A": "Python", "B": "C", "C": "FORTRAN", "D": "Java"}, "C"),
 (7, "Trong các lĩnh vực sau, tin học chưa thật sự thay thế được con người hoàn toàn là", {"A": "Tính toán phép toán phức tạp với tốc độ cao", "B": "Lưu trữ và truy xuất dữ liệu lớn", "C": "Phân tích cảm xúc, tâm lí con người một cách trọn vẹn", "D": "Điều khiển dây chuyền sản xuất tự động"}, "C"),
 (8, "Cuộc cách mạng công nghiệp lần thứ tư gắn liền với nhóm công nghệ nào?", {"A": "Động cơ hơi nước", "B": "Điện năng và sản xuất hàng loạt", "C": "Máy tính điện tử đơn thuần", "D": "AI, IoT, điện toán đám mây và dữ liệu lớn"}, "D"),
 (9, "Phát biểu nào đúng khi nói về mạng LAN?", {"A": "LAN là mạng toàn cầu không có chủ sở hữu", "B": "LAN có phạm vi nhỏ, thường thuộc sở hữu của một tổ chức", "C": "LAN không cần thiết bị kết nối", "D": "LAN chính là Internet"}, "B"),
 (10, "Dịch vụ nào sau đây thuộc nhóm SaaS của điện toán đám mây?", {"A": "Máy chủ ảo Amazon EC2", "B": "Dịch vụ lưu trữ Dropbox", "C": "Gmail", "D": "Nền tảng Google App Engine"}, "C"),
 (11, "IoT là viết tắt của cụm từ nào?", {"A": "Internet of Things", "B": "Intel of Things", "C": "Internet of Teacher", "D": "Information of Technology"}, "A"),
 (12, "Hành vi nào sau đây là ứng dụng của IoT?", {"A": "Viết thư tay gửi bạn bè", "B": "Công tơ điện tử tự gửi số liệu tiêu thụ về công ty điện", "C": "Đọc sách in trong thư viện", "D": "Ghi chép sổ sách bằng bút mực"}, "B"),
 (13, "Phần mềm độc hại nào là chương trình hoàn chỉnh, tự lan qua mạng mà không cần gắn vào tệp khác?", {"A": "Virus", "B": "Worm", "C": "Trojan", "D": "Tệp văn bản"}, "B"),
 (14, "Khi bị bắt nạt trên mạng, cách xử lí ĐÚNG là", {"A": "Im lặng và xoá hết tin nhắn", "B": "Trả lời gay gắt để đáp trả", "C": "Lưu bằng chứng, chặn tài khoản và chia sẻ với bố mẹ, thầy cô", "D": "Đăng thông tin cá nhân của người đó để trả đũa"}, "C"),
 (15, "Mật khẩu nào yếu nhất?", {"A": "Tin@Hoc10#2026", "B": "123456", "C": "Nghia@1998!x", "D": "Kt#7pQ2!z"}, "B"),
 (16, "Hành vi nào sau đây vi phạm bản quyền?", {"A": "Tự viết bài rồi đăng lên blog cá nhân", "B": "Dùng ảnh có giấy phép Creative Commons và ghi nguồn", "C": "Chép đĩa cài phần mềm bản quyền đem cho nhiều người", "D": "Trích dẫn một câu của bài báo, ghi rõ tác giả và nguồn"}, "C"),
 (17, "Luật An ninh mạng số 24/2018/QH14 có hiệu lực từ", {"A": "1/1/2007", "B": "1/1/2013", "C": "1/1/2019", "D": "17/6/2021"}, "C"),
 (18, "Chia sẻ thông tin sai sự thật trên mạng xã hội có thể bị xử phạt theo", {"A": "Điều 101 Nghị định 15/2020/NĐ-CP", "B": "Điều 25 Luật Sở hữu trí tuệ", "C": "Luật Giao dịch điện tử 2005", "D": "Quy chuẩn bàn phím máy tính"}, "A"),
 (19, "3 MB bằng bao nhiêu KB?", {"A": "300", "B": "3 000", "C": "3 072", "D": "3 145 728"}, "C"),
 (20, "Một người phát tán tin đồn sai sự thật làm doanh nghiệp mất đơn hàng. Đây là", {"A": "Hành vi hợp pháp vì Internet tự do", "B": "Hành vi vi phạm Luật An ninh mạng và có thể bị xử phạt hành chính, bồi thường", "C": "Hành vi chỉ vi phạm đạo đức, không bị xử lí", "D": "Hành vi được khuyến khích"}, "B"),
]
EXAM_DS = [
 (21, "Đọc đoạn thông tin: «Lan dùng điện thoại thông minh để học trực tuyến, lưu bài giảng lên Google Drive, "
       "sau đó dùng Google Translate để dịch một đoạn tài liệu tiếng Anh. Lan đặt mật khẩu là 123456 cho mọi tài khoản.» "
       "Hãy đánh giá các nhận định sau:",
  [("a", "Google Drive là một dịch vụ điện toán đám mây."),
   ("b", "Google Translate là công cụ xử lí thông tin giúp dịch tự động văn bản."),
   ("c", "Đặt cùng một mật khẩu đơn giản cho mọi tài khoản là cách bảo vệ dữ liệu tốt."),
   ("d", "Học trực tuyến là một thay đổi tích cực của phương thức học tập nhờ mạng máy tính.")]),
 (22, "Đọc tình huống: «Một trang web sao chép toàn bộ bài viết và hình ảnh của báo X để đăng lại, không xin phép, "
       "không ghi nguồn. Một độc giả bấm Share bài viết sai sự thật về một công ty, khiến bài lan truyền rất nhanh.» "
       "Hãy đánh giá các nhận định sau:",
  [("a", "Trang web đã vi phạm quyền tác giả theo Luật Sở hữu trí tuệ."),
   ("b", "Việc ghi nguồn đầy đủ sẽ tự động miễn trừ mọi trách nhiệm khi dùng toàn bộ tác phẩm."),
   ("c", "Bấm Share vào bài viết sai sự thật góp phần lan truyền thông tin sai và có thể bị xem xét xử lí."),
   ("d", "Có thể căn cứ Luật An ninh mạng và Nghị định 15/2020/NĐ-CP để đánh giá hành vi chia sẻ tin sai.")]),
]
EXAM_TL = [
 (1, "(Thông hiểu – 1,0 điểm) Em hãy phân biệt thông tin và dữ liệu, nêu ví dụ minh hoạ và trình bày ba bước xử lí thông tin của máy tính."),
 (2, "(Vận dụng – 1,0 điểm) Một tệp video có dung lượng 2,5 GB. Em hãy đổi dung lượng đó sang MB và KB. Nếu ổ USB còn trống 3 000 MB thì có chép được tệp video này vào USB không? Giải thích."),
 (3, "(Vận dụng cao – 1,0 điểm) Một công ty tự ý lấy bài viết và video minh hoạ từ trang web của nhà sản xuất game nước ngoài đăng lên trang web của mình, không xin phép. "
      "Em hãy vận dụng các văn bản pháp luật đã học để: (a) xác định tính hợp pháp của hành vi; (b) chỉ ra căn cứ pháp lí; "
      "(c) nêu hậu quả và cách xử lí đúng."),
]

story.append(H2("VI.1. ĐỀ BÀI"))
story.append(H3("A. Phần trắc nghiệm (7,0 điểm)"))
story.append(P("<b>Câu 1 – 20 (mỗi câu 0,25 điểm):</b> chọn phương án đúng nhất (A, B, C hoặc D).", "tiny"))
for num, q, opts, ans in EXAM_TN:
    line = "   ".join("<b>" + k + ".</b> " + esc(v) for k, v in opts.items())
    story.append(Paragraph('<font color="#17365D"><b>Câu ' + str(num) + ".</b></font> " + esc(q), ST["q"]))
    story.append(Paragraph(line, ST["opt"]))
    story.append(Spacer(1, 2))
story.append(P("<b>Câu 21 – 22 (mỗi câu 1,0 điểm):</b> với mỗi ý a), b), c), d) hãy chọn Đúng hoặc Sai.", "tiny"))
for num, stem, statements in EXAM_DS:
    story.append(Paragraph('<font color="#17365D"><b>Câu ' + str(num) + ".</b></font> " + esc(stem), ST["q"]))
    for label, txt in statements:
        story.append(Paragraph("<b>" + label + ")</b> " + esc(txt) + "  ………  Đúng / Sai", ST["opt"]))
    story.append(Spacer(1, 3))
story.append(H3("B. Phần tự luận (3,0 điểm)"))
for num, q in EXAM_TL:
    story.append(Paragraph('<font color="#17365D"><b>Câu ' + str(num) + ".</b></font> " + esc(q), ST["q"]))
    story.append(Spacer(1, 14))
story.append(PageBreak())

story.append(H2("VI.2. ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM ĐỀ THI THỬ"))
story.append(H3("A. Đáp án phần trắc nghiệm"))
ans_exam = []
for start in (0, 10):
    ans_exam.append(["Câu"] + [str(n) for n, *_ in EXAM_TN[start:start+10]])
    ans_exam.append(["Đáp án"] + [a for _, _, _, a in EXAM_TN[start:start+10]])
t = Table([[Paragraph(esc(c), ST["cellb"] if r % 2 == 0 else ST["cell"]) for c in row]
           for r, row in enumerate(ans_exam)], colWidths=[52] + [41.3]*10)
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE),
                       ("BACKGROUND", (0, 0), (-1, 0), BGBLUE),
                       ("BACKGROUND", (0, 2), (-1, 2), BGBLUE),
                       ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                       ("TOPPADDING", (0, 0), (-1, -1), 4),
                       ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
story.append(t)
story.append(H4("Giải thích ngắn các câu dễ nhầm"))
for x in [
    "Câu 2: 1 GB = 1 024 MB (không phải 1 000). Câu 19: 3 MB = 3 × 1 024 = 3 072 KB.",
    "Câu 7: máy tính vượt trội về tính toán, lưu trữ, tự động hoá nhưng chưa thay thế hoàn toàn con người trong phân tích cảm xúc, tâm lí.",
    "Câu 10: Gmail, Google Docs, Zoom là SaaS; Dropbox/Google Drive là IaaS (lưu trữ); Google App Engine là PaaS.",
    "Câu 13: Worm là chương trình hoàn chỉnh tự lan qua mạng; virus chỉ là đoạn mã phải gắn vào chương trình khác.",
    "Câu 16: sao chép đĩa cài phần mềm bản quyền cho nhiều người là vi phạm bản quyền; trích dẫn hợp lí và dùng ảnh CC có ghi nguồn thì hợp pháp.",
    "Câu 20: tin sai sự thật gây thiệt hại vi phạm Luật An ninh mạng (Điều 8) và bị xử phạt theo Nghị định 15/2020/NĐ-CP.",
]:
    story.append(B(x))
story.append(H4("Đáp án câu đúng/sai"))
story.append(TB([
    ["Câu", "a", "b", "c", "d", "Giải thích ngắn"],
    ["21", "Đ", "Đ", "S", "Đ", "Google Drive là dịch vụ đám mây; Google Translate dịch tự động văn bản; mật khẩu 123456 dùng cho mọi tài khoản là rất yếu; học trực tuyến là thay đổi tích cực nhờ mạng."],
    ["22", "Đ", "S", "Đ", "Đ", "Sao chép toàn bộ tác phẩm không phép vi phạm Điều 28 Luật SHTT; ghi nguồn không thay thế sự cho phép khi dùng toàn bộ tác phẩm; Share tin sai tiếp tay lan truyền và có thể bị xử lí; căn cứ Luật An ninh mạng Điều 8, Nghị định 15/2020 Điều 101."],
], [36, 22, 22, 22, 22, 341], font="cellsm"))
story.append(H4("Hướng dẫn chấm phần tự luận"))
story.append(QA("Câu 1 (1,0đ)",
  "Yêu cầu: phân biệt thông tin và dữ liệu, nêu ví dụ, trình bày ba bước xử lí thông tin.",
  "Phân biệt đúng (0,3đ): thông tin là hiểu biết thu được, gắn với nhận thức; dữ liệu là thông tin đã đưa vào máy tính dưới dạng chữ, số, ảnh, âm thanh… Ví dụ đúng (0,3đ): dãy nhiệt độ 37; 39; 40 là dữ liệu; kết luận «bạn bị sốt» là thông tin. Ba bước (0,4đ): (1) tiếp nhận dữ liệu, (2) xử lí dữ liệu, (3) đưa ra kết quả (có thể lưu trữ và truyền đi)."))
story.append(Spacer(1, 4))
story.append(QA("Câu 2 (1,0đ)",
  "Yêu cầu: đổi 2,5 GB sang MB, KB và quyết định có chép vào USB trống 3 000 MB không.",
  "2,5 GB = 2,5 × 1 024 = 2 560 MB (0,3đ). 2 560 MB = 2 560 × 1 024 = 2 621 440 KB (0,3đ). So sánh: 3 000 MB > 2 560 MB nên USB còn đủ chỗ, chép được tệp video (0,3đ). Nêu đúng quy tắc đổi: lớn sang nhỏ nhân 1 024, nhỏ sang lớn chia 1 024 (0,1đ). Lưu ý: nếu em quy đổi theo 1 GB = 1 000 MB thì sai với quy ước của SGK."))
story.append(Spacer(1, 4))
story.append(QA("Câu 3 (1,0đ)",
  "Yêu cầu: xác định tính hợp pháp, nêu căn cứ pháp lí, hậu quả và cách xử lí đúng.",
  "(a) Kết luận: hành vi của công ty là KHÔNG hợp pháp, vi phạm bản quyền tác giả (0,25đ). (b) Căn cứ: các khoản 7, 8, 10 Điều 28 Luật Sở hữu trí tuệ 50/2005/QH11 (sửa đổi 2019) về hành vi xâm phạm quyền tác giả; Nghị định 72/2013/NĐ-CP về quản lí, cung cấp, sử dụng thông tin trên mạng; Nghị định 131/2013/NĐ-CP về xử phạt hành chính quyền tác giả; có thể tham chiếu Điều 12 Luật Công nghệ thông tin (0,35đ). (c) Hậu quả và xử lí: phải gỡ bỏ bài viết/video vi phạm, xin lỗi và bồi thường thiệt hại cho chủ sở hữu; bị phạt hành chính (5–10 triệu đồng với công bố trái phép, 15–35 triệu đồng với sao chép trái phép), uy tín bị ảnh hưởng; trường hợp nghiêm trọng có thể bị truy cứu trách nhiệm hình sự. Cách đúng: liên hệ xin phép, kí thoả thuận và trả phí bản quyền, hoặc chỉ trích dẫn hợp lí một phần nhỏ theo Điều 25 Luật SHTT kèm ghi rõ tên tác giả, nguồn và ngày công bố (0,4đ)."))
story.append(BOX([P("<b>Thang điểm tổng:</b> 20 TN × 0,25 = 5,0 điểm; 2 câu ĐS × 1,0 = 2,0 điểm (mỗi ý đúng 0,25 điểm); "
                    "3 câu TL × 1,0 = 3,0 điểm. Tổng 10 điểm. Quy đổi sang thang 10 theo đúng số điểm đạt được.", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(PageBreak())

# ==========================================================================
# PHAN VII - CHIEN LUOC ON TAP
# ==========================================================================
story.append(H1("PHẦN VII", "CHIẾN LƯỢC ÔN TẬP VÀ MẸO LÀM BÀI"))
story.append(H2("VII.1. Lộ trình ôn tập 5 ngày"))
story.append(TB([
    ["Ngày", "Nội dung ôn", "Sản phẩm cần đạt được"],
    ["Ngày 1", "Phần I + Phần II.1 (Chủ đề A): dữ liệu – thông tin, đơn vị lưu trữ, thiết bị thông minh, thành tựu tin học, kĩ năng số", "Làm xong 8 câu TN đầu (V.1) và trả lời được 14 câu A1–A3 ở Phần IV"],
    ["Ngày 2", "Phần II.2 (Chủ đề B): LAN/Internet, đám mây, IoT, dịch vụ web, malware, an toàn thông tin", "Làm TN 19–40, ĐS 3, ĐS 4 và trả lời 15 câu B1–B2 ở Phần IV"],
    ["Ngày 3", "Phần II.3 (Chủ đề D): bản quyền, 4 văn bản luật + 2 nghị định xử phạt, chia sẻ an toàn, xác định tính hợp pháp", "Làm TN 41–60, ĐS 5, ĐS 6, TL 13–15; học thuộc bảng luật ở III.2/II.3.1c"],
    ["Ngày 4", "Phần III (bảng tra cứu nhanh) + Phần IV (đọc lại toàn bộ 35 câu hỏi – đáp án)", "Tự giải thích lại 35 yêu cầu cần đạt không nhìn sách; lập danh sách ý còn yếu"],
    ["Ngày 5", "Làm đề thi thử Phần VI trong đúng 45 phút, tự chấm điểm, đối chiếu đáp án và ôn lại các câu sai", "Đạt tối thiểu 7/10; không còn câu nào sai ở mức Nhận biết và Thông hiểu"],
], [52, 243, 170], font="cellsm"))
story.append(H2("VII.2. Mẹo làm bài theo từng dạng"))
story.append(TB([
    ["Dạng bài", "Mẹo cụ thể"],
    ["Trắc nghiệm 4 lựa chọn", "Đọc kĩ câu hỏi, gạch chân từ khoá (KHÔNG, SAI, ĐÚNG NHẤT). Loại dần phương án sai chắc chắn trước. Với câu đổi đơn vị, viết ngay dãy B → KB → MB → GB ra nháp rồi nhân/chia 1 024. Không bỏ trống câu nào."],
    ["Câu đúng/sai", "Đọc từng ý độc lập; một câu có thể có cả ý đúng và ý sai. Tìm các từ «luôn luôn», «không bao giờ», «chỉ», «hoàn toàn» – thường là dấu hiệu của ý sai. Ghi rõ Đ/S cho cả 4 ý."],
    ["Câu tự luận TH/VD", "Trả lời theo cấu trúc 3 phần: nêu khái niệm → giải thích/ phân tích → ví dụ cụ thể. Với bài toán đổi đơn vị phải ghi rõ công thức, phép tính và đơn vị cuối cùng."],
    ["Câu vận dụng cao (Chủ đề D)", "Dùng quy trình 4 bước: mô tả hành vi → đối chiếu văn bản luật (gọi tên điều, luật/nghị định cụ thể) → kết luận hợp pháp hay không → nêu hậu quả, chế tài và cách xử lí đúng. Có ví dụ minh hoạ sẽ được điểm tối đa."],
    ["Quản lí thời gian", "Dành 20–22 phút cho trắc nghiệm, 8 phút cho câu ĐS, 12–15 phút cho 3 câu tự luận, 3 phút rà soát lại đáp án và thông tin cá nhân trên bài làm."],
], [100, 365], font="cellsm"))
story.append(H2("VII.3. Bảng tự kiểm tra nhanh trước khi vào phòng thi"))
for x in [
    "Em có nhớ 1 B = 8 bit và mỗi bậc hơn kém 1 024 lần không?",
    "Em có phân biệt được dữ liệu – thông tin và nêu ví dụ ngay lập tức không?",
    "Em có kể được 3 thiết bị thông minh và giải thích được vì sao chúng là hệ thống xử lí thông tin không?",
    "Em có nhớ 4 mốc phát triển tin học (1957, 1964, 1983, 1992) và 4 cuộc cách mạng công nghiệp không?",
    "Em có so sánh được LAN – Internet theo 3 tiêu chí và nêu 3 dịch vụ đám mây (SaaS, PaaS, IaaS) kèm ví dụ không?",
    "Em có viết được khái niệm IoT và nêu 3 ví dụ ứng dụng kèm lợi ích không?",
    "Em có phân biệt virus – worm – trojan và biết 4 chế độ quét của Windows Defender không?",
    "Em có nêu được 6 biện pháp tự bảo vệ dữ liệu cá nhân và 5 cách phòng vệ khi bị bắt nạt không?",
    "Em có nhớ tên 4 văn bản luật/nghị định chính (Luật CNTT 2006, Luật An ninh mạng 2018, NĐ 72/2013, Luật SHTT) và 2 nghị định xử phạt (131/2013, 15/2020) không?",
    "Em có viết được quy trình 4 bước xác định tính hợp pháp của một hành vi không?",
]:
    story.append(B("☐  " + x))
story.append(BOX([P("Nếu em trả lời «có» cho ít nhất 9/10 câu trên, em đã sẵn sàng cho bài kiểm tra giữa kì I. "
                    "Chúc em ôn tập hiệu quả và đạt kết quả cao!", "note")],
                 bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(PageBreak())

# ==========================================================================
# PHU LUC A - NGUYEN VAN TAI LIEU GOC
# ==========================================================================
def raw_source_table(tbl, widths, header_rows, small=True, center_from=None):
    """Tai hien nguyen ven mot bang trong file .docx (ke ca gop cot, gop dong)."""
    ncol = len(widths)
    grid, spans = [], []
    for r_i, row in enumerate(tbl["rows"]):
        cells = [""] * ncol
        col = 0
        for c in row:
            span = c["span"]
            txt = c["text"]
            if c["vmerge"] == "continue":
                txt = ""
            if col < ncol:
                cells[col] = txt.replace("\t", " ").strip()
            if span > 1 and col + span - 1 < ncol:
                spans.append(("SPAN", (col, r_i), (col + span - 1, r_i)))
            col += span
        grid.append(cells)
    sty = "celltiny" if small else "cell"
    hsty = "thtiny" if small else "th"
    body = [[Paragraph(esc(cell), ST[hsty if r_i < header_rows else sty]) for cell in row]
            for r_i, row in enumerate(grid)]
    t = Table(body, colWidths=widths, repeatRows=header_rows)
    cmds = [("GRID", (0, 0), (-1, -1), 0.4, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 1.2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 1.2),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("BACKGROUND", (0, 0), (-1, header_rows - 1), NAVY)]
    cmds.extend(spans)
    cmds.append(("ALIGN", (0, 0), (0, -1), "CENTER"))
    if center_from is not None:
        cmds.append(("ALIGN", (center_from, 0), (-1, -1), "CENTER"))
    for i in range(header_rows, len(body)):
        if i % 2 == 1:
            cmds.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F8FAFC")))
    t.setStyle(TableStyle(cmds))
    return t

story.append(H1("PHỤ LỤC A", "NGUYÊN VĂN TÀI LIỆU GỐC (MA TRẬN VÀ ĐẶC TẢ ĐỀ)"))
story.append(P("Toàn bộ nội dung dưới đây được trích nguyên văn từ tệp <b>«MA TRAN GIUA KI I - LOP 10.docx»</b>. "
               "Hai bảng được tái hiện đầy đủ các ô, kể cả ô gộp; dấu «/» hoặc khoảng trống trong bản gốc được giữ nguyên. "
               "Đây là căn cứ để đối chiếu với các phần đã biên soạn ở trên."))
story.append(H2("A.1. Các dòng thông tin chung (nguyên văn)"))
for it in SOURCE_DATA:
    if it["type"] == "p" and it["text"].strip():
        story.append(P(it["text"], "tinyj"))
        story.append(Spacer(1, 2))
story.append(H2("A.2. Bảng ma trận đề kiểm tra giữa kì I (nguyên văn, 18 cột)"))
t1 = [it for it in SOURCE_DATA if it["type"] == "tbl"][0]
widths1 = [18, 78, 110] + [14] * 14 + [61]
story.append(raw_source_table(t1, widths1, 3, center_from=3))
story.append(P("Ghi chú: cột «Tổng% điểm» và các dòng «Tổng», «Tỉ lệ % từng mức độ nhận thức», «Tỉ lệ chung» "
               "được giữ nguyên số liệu như bản gốc (có một vài ô gộp chéo giữa hai mức độ). Bản đọc dễ hơn ở mục I.2.", "tinyj"))
story.append(PageBreak())
story.append(H2("A.3. Bảng đặc tả đề kiểm tra giữa kì I (nguyên văn, 12 cột)"))
t2 = [it for it in SOURCE_DATA if it["type"] == "tbl"][1]
widths2 = [18, 70, 88, 180] + [13] * 8
story.append(raw_source_table(t2, widths2, 2, center_from=4))
story.append(P("Ghi chú: các yêu cầu cần đạt trong cột thứ tư chính là nguồn của 35 câu hỏi – đáp án mẫu ở Phần IV. "
               "Bảng đối chiếu ở Phụ lục B liệt kê từng yêu cầu một.", "tinyj"))
story.append(PageBreak())

# ==========================================================================
# PHU LUC B - BANG DOI CHIEU 100% YEU CAU CAN DAT
# ==========================================================================
story.append(H1("PHỤ LỤC B", "BẢNG ĐỐI CHIẾU 100% YÊU CẦU CẦN ĐẠT"))
story.append(P("Bảng này chứng minh <b>không có yêu cầu cần đạt nào của bản đặc tả bị bỏ sót</b>. "
               "Mỗi dòng là một ý trong cột «Mức độ kiến thức, kĩ năng cần kiểm tra, đánh giá» của Phụ lục A.3. "
               "Cột «Câu hỏi – đáp án» trỏ tới đúng câu ở Phần IV; cột «Luyện tập» trỏ tới ngân hàng câu hỏi ở Phần V/VI."))

def short(s, n=118):
    s = " ".join(s.split())
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"

map_rows = [["Mã", "Yêu cầu cần đạt (trích)", "Mức độ", "Kiến thức", "Câu hỏi – đáp án", "Luyện tập"]]
for code, unit, level, yccd, ques, ans, theory, practice in REQUIREMENTS:
    map_rows.append([code, short(yccd), level, theory, "Phần IV · " + code, practice])
story.append(TB(map_rows, [58, 175, 48, 45, 72, 67], font="cellsm"))
story.append(BOX([
    P("<b>Thống kê độ bao phủ:</b> 35/35 yêu cầu cần đạt (100%) · 6/6 đơn vị kiến thức · 4/4 mức độ nhận thức. "
      "Số câu hỏi – đáp án mẫu: 35. Số câu luyện tập bổ sung: 60 trắc nghiệm + 8 câu đúng/sai + 15 câu tự luận "
      "+ 20 trắc nghiệm + 2 câu đúng/sai + 3 câu tự luận của đề thi thử = <b>108 câu</b> (đều có đáp án).", "note"),
], bg=BGTEAL, border=TEAL, leftbar=TEAL))
story.append(P("<b>Kết luận:</b> Tài liệu gốc (ma trận + đặc tả) được giữ nguyên vẹn ở Phụ lục A; "
               "toàn bộ nội dung cần kiểm tra được giải thích ở Phần II–III, chuyển hoá thành câu hỏi có đáp án ở Phần IV "
               "và luyện tập có đáp án ở Phần V–VI. Đề cương vì thế vừa là bản tóm tắt kiến thức, vừa là ngân hàng đề thi.", "note"))
story.append(Spacer(1, 6))
story.append(P("— HẾT TÀI LIỆU —", "bodyc"))

# ==========================================================================
# DUNG PDF
# ==========================================================================
PAGE_W, PAGE_H = A4
FRAME_X = 65
FRAME_W = PAGE_W - 2 * FRAME_X
FRAME_Y = 52
FRAME_H = PAGE_H - 58 - FRAME_Y

class ReviewDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if not hasattr(flowable, "style"):
            return
        name = getattr(flowable.style, "name", "")
        if name not in ("h1t", "h2"):
            return
        level = 0 if name == "h1t" else 1
        text = flowable.getPlainText()
        self._bk = getattr(self, "_bk", 0) + 1
        key = "sec-%d-%d" % (level, self._bk)
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=(level == 0))
        self.notify("TOCEntry", (level, text, self.page))

def decorate(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setFont("DV", 7.2)
        canvas.setFillColor(GRAY)
        canvas.drawString(FRAME_X, PAGE_H - 38, "ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I  ·  TIN HỌC 10 – KẾT NỐI TRI THỨC")
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.6)
        canvas.line(FRAME_X, PAGE_H - 43, PAGE_W - FRAME_X, PAGE_H - 43)
        canvas.line(FRAME_X, 43, PAGE_W - FRAME_X, 43)
        canvas.setFont("DV", 7.2)
        canvas.drawString(FRAME_X, 32, "Biên soạn từ Ma trận & Đặc tả đề kiểm tra giữa kì I – Tin học 10 (định hướng ICT)")
        canvas.drawRightString(PAGE_W - FRAME_X, 32, "Trang %d" % doc.page)
    else:
        canvas.setFillColor(TEAL)
        canvas.rect(0, PAGE_H - 12, PAGE_W, 12, stroke=0, fill=1)
        canvas.setFont("DV", 7.2)
        canvas.setFillColor(GRAY)
        canvas.drawCentredString(PAGE_W / 2, 28, "Tài liệu ôn tập dành cho học sinh lớp 10  ·  Tháng 10/2026")
    canvas.restoreState()

# --------------------------------------------------------------------------
# Kiem chứng du lieu cau hoi - dap an
# --------------------------------------------------------------------------
assert len(REQUIREMENTS) == 35, "Phai co 35 yeu cau can dat"
assert len(TN_BANK) == 60 and [n for n, *_ in TN_BANK] == list(range(1, 61))
assert all(a in opts for _n, _q, opts, a, _e in TN_BANK), "Dap an TN khong nam trong lua chon"
assert len(DS_BANK) == 8 and [n for n, *_ in DS_BANK] == list(range(1, 9))
assert all(len(st) == 4 and len(a) == 4 and set(a) <= {"Đ", "D", "S"}
           for _n, _stem, st, a, _e in DS_BANK), "Dap an DS khong hop le"
assert len(TL_BANK) == 15 and [n for n, *_ in TL_BANK] == list(range(1, 16))
assert len(EXAM_TN) == 20 and all(a in opts for _n, _q, opts, a in EXAM_TN)
assert len(EXAM_DS) == 2 and all(len(st) == 4 for _n, _stem, st in EXAM_DS)
assert len(EXAM_TL) == 3

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "De-cuong-on-tap-giua-ki-I-Tin-hoc-10.pdf")
doc = ReviewDoc(OUT, pagesize=A4,
                leftMargin=FRAME_X, rightMargin=FRAME_X,
                topMargin=58, bottomMargin=FRAME_Y,
                title="Đề cương ôn tập kiểm tra giữa kì I – Tin học 10 (Kết nối tri thức)",
                author="Biên soạn từ ma trận và đặc tả đề kiểm tra giữa kì I",
                subject="Đề cương ôn tập giữa kì I môn Tin học 10 – định hướng ICT")
frame = Frame(FRAME_X, FRAME_Y, FRAME_W, FRAME_H, id="main",
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=decorate)])
doc.multiBuild(story, maxPasses=4)
print("Da tao:", OUT)
print("Tong so cau hoi co dap an:", len(REQUIREMENTS), "+", len(TN_BANK), "+", len(DS_BANK), "+",
      len(TL_BANK), "+", len(EXAM_TN), "+", len(EXAM_DS), "+", len(EXAM_TL))
