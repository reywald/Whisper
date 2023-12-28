import pytest
from pathvalidate import ValidationError

from app.speech_to_text import get_audio_file
from app.utilities import FileTypeError


def test_file_not_passed():
    """
    Test the get_audio_file when it does not receive a filename
    """

    with pytest.raises(TypeError):
        audio = get_audio_file()


@pytest.mark.parametrize("file_name", [
    "e72Q23Z8o7IbytZcLTOx",
    "JCLBrD2E5JHskaOiqj9o",
    "ok5YQ5mqUKaZLbiNF164",
    "nfCCfNzQwRu95AX6x6vt",
    "eAiO2o5QmAjRwGTbhDxF",
    "**]{05-!0-1x|5&z8!@*",
    "o:\\dp0(RR6(lGwmo\\ (sGi3x(-ctEB1sRMcpC9qVNjfInSv1IsFV\\(uxMsMAgI1q)66nskNOyAWEPsrnSAlnb8Jy9PZdWS9XfckF\\r4PosQbrEQgX7iSGKP1ULPYcM\\F4WZDgJxuXNqly0Qcr6h95Xs1OeKD\\BqE5-5HqtssS-HGqdXkc9Tcbtovz)aSM\\Cdy-jy(NHKk)HCXdJZwfk7yeB9T\\n4n18znohSG-QXWrLhpRqN9OUQRK\\MStqFTiX)weBOrgCuodxJ3hX)4PkWWpqU\\pC_2ZHPWoI49rS0C5W2tLL)d-m_JCN.ppt",
    "r:\\bXHgOrjtLT9eA)MR5hlhs\\cJ)VUPmJHDvRZW9AHP0IdVvxvGK\\CoLgajYSl4QKzjNPe2pBahyX6kIdu\\rgog-73Jbab 9tq\\oOyxN_20gLNYVCFRDM2d\\w6W8UCJqCgKGU0V(_zayv51 svAhD\\eBUkzW1n-)sMr BVr 9-Ejrv\\IR XCU-eXItDr_IMcGoWhxEOcRkOHrLA\\y4qRFvqOOh4KZ4olBD1)yQZ(MD ezr3 7F1kSJhwShNB7P00rBneF19CiKizK7lgbfSYiH\\ZL2anhQ4UWTPDVO6J)LVFlwGNR6PWLxM.avi",
    "i:\\36H9xN9EF8tuAnytLSC_NTUzJnzxdzEZsnefImWWrk\\ 2gpvaVQ1oCywgdsJ(hL c_ix202d\\606n(kl V0zCQyJJnyQILZDxhC3(3cWRb8JXwBk)YIzW5ni5DVk6Zb_p(Y9CK)dP89X5jyIuJds2FPc_8xRrABZrM(x5unx-WF(dn90Ox3i2s9Hn_aiTuyh-dm-0R)\\LuNieTgP3LvaTmQ17wd3G_tBt(hkPq1pZ EG6(U IHl6aRWfZ7iEYzoT58IqWWJ6Iw1HpPEmrWwtz6_0A)Z xVj4H1c1(vd2xIpYac.mp3",
    "E:\\0RaFTJ2QNcrGKNWz3p50huNZZlVKDVJxiAa O8gcm_8)7hT\\TPM2vSa3cVa-7KDx_3fAdrIVDW2lfUOEwOUN3\\sjPPINmaO7m086C Mko(_Jr3R7b(YD1n22mLgvTR8EV-94IeVJ_H8wrIzQWjnT13(V\\K4pyJ4M(Ra6SyWRgK4JHnIYDviCuhSiyvncdkOkgrY3rdkLshXCwj0phP7aEA4MGaYzQmB2SZmv(bo5DpFN1e8Lv8akMCgyskEVV2a2fiokRJmGv5PV)LHOGuT3NxfNWEH_GzPbi9baJI9DMJHKs2.tiff"
    ">=2|!*/56x>0<7x]#;/",
    "!*11y0;y]](~$\\C?=_3y",
    "<01*&D}z@_!*D~9<B!>-",
    "1&]!9|~yx7B3y*+=1^|",
])
def test_invalid_filename(file_name):
    """
    Test the get_audio_file when it does not receive a valid filename
    """

    with pytest.raises((FileNotFoundError, ValidationError, Exception)):
        audio = get_audio_file(file_name)


@pytest.mark.parametrize("file_name", [
    "o:\\dp0(RR6(lGwmo\\ (sGi3x(-ctEB1sRMcpC9qVNjfInSv1IsFV\\(uxMsMAgI1q)66nskNOyAWEPsrnSAlnb8Jy9PZdWS9XfckF.ppt",
    "r:\\bXHgOrjtLT9eA)MR5hlhs\\cJ)VUPmJHDvRZW9AHP0IdVvxvGK\\CoLgajYSl4QKzjNPe2pBahyX6kIdu\\rgog-73Jbab 9tq\\oOyxN_20gLNYVCFRDM2d\\w6W8UCJqCgKGU0V(_zayv51 svAhD\\eBUkzW1.avi",
    "i:\\36H9xN9EF8tuAnytLSC_NTUzJnzxdzEZsnefImWWrk\\ 2gpvaVQ1oCywgdsJ(hL c_ix202d\\606n(kl V0zCQyJJnyQILZDxhC3(3cWRb8JXwBk)YIzW5ni5DVk6Zb_p(Y9CK)dP891(vd2xIpYac.mp4",
    "E:\\0RaFTJ2QNcrGKNWz3p50huNZZlVKDVJxiAa O8gcm_8)7hT\\TPM2vSa3cVa-7KDx_3fAdrIVDW2lfUOEwOUN3\\sjPPINmaO7m086CH_GzPbi9baJI9DMJHKs2.tiff"
])
def test_file_not_mp3(file_name):
    """
    Test the get_audio_file when it does not receive a .mp3 file
    """

    with pytest.raises(FileTypeError):
        audio = get_audio_file(file_name)
