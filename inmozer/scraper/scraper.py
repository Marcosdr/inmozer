from urllib.request import Request, urlopen
import gzip


def html_parse(content: str):
    pass


def scrap(url: str):
    req = create_request(url)
    web = urlopen(req)

    content = gzip.decompress(web.read()).decode('utf-8')
    #html_parse(content)
    return content


def create_request(url: str) -> Request:
    req: Request = Request(url)
    # req.add_header(":authority", "www.idealista.com")
    # req.add_header(":path", "/venta-viviendas/palma-de-mallorca-balears-illes/")
    req.add_header("accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
    req.add_header("accept-encoding", "gzip, deflate, br")
    req.add_header("accept-language", "en-US,en;q=0.9")
    req.add_header("cache-control", "max-age=0")

    req.add_header("sec-ch-ua", ' Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"')
    req.add_header("sec-ch-ua-mobile", "?0")
    req.add_header("sec-ch-ua-platform", "Windows")
    req.add_header("sec-fetch-dest", "document")
    req.add_header("sec-fetch-mode", "navigate")
    req.add_header("sec-fetch-site", "none")
    req.add_header("sec-fetch-user", "?1")
    req.add_header("upgrade-insecure-requests", "1")


    req.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36")
    req.add_header("cookie", 'atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%225d40be9d-ea0f-48a7-8659-f35aaf514a09%22%2C%22options%22%3A%7B%22end%22%3A%222023-02-13T07%3A24%3A16.418Z%22%2C%22path%22%3A%22%2F%22%7D%7D; didomi_token=eyJ1c2VyX2lkIjoiMTdlNGQyYzQtYWQ1Ni02NDdmLWExMDQtYmFlMTY3MGZhN2VlIiwiY3JlYXRlZCI6IjIwMjItMDItMDFUMTc6NDk6MzQuNjAzWiIsInVwZGF0ZWQiOiIyMDIyLTAyLTAxVDE3OjQ5OjM0LjYwM1oiLCJ2ZXJzaW9uIjoyLCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImFuYWx5dGljcy1IcEJKcnJLNyIsImdlb2xvY2F0aW9uX2RhdGEiXX0sInZlbmRvcnMiOnsiZW5hYmxlZCI6WyJnb29nbGUiLCJjOm1peHBhbmVsIiwiYzphYnRhc3R5LUxMa0VDQ2o4IiwiYzpob3RqYXIiLCJjOnlhbmRleG1ldHJpY3MiLCJjOmJlYW1lci1IN3RyN0hpeCIsImM6YXBwc2ZseWVyLUdVVlBMcFlZIiwiYzp0ZWFsaXVtY28tRFZEQ2Q4WlAiLCJjOmlkZWFsaXN0YS1MenRCZXFFMyIsImM6aWRlYWxpc3RhLWZlUkVqZTJjIl19LCJhYyI6IkFGbUFDQUZrLkFBQUEifQ==; euconsent-v2=CPTtLAAPTtLAAAHABBENCACoAP_AAAAAAAAAF5wBAAIAAtAC2AvMAAABAaADAAEERiUAGAAIIjFIAMAAQRGIQAYAAgiMOgAwABBEYJABgACCIwyADAAEERhUAGAAIIjA.f_gAAAAAAAAA; _fbp=fb.1.1643737775272.1578197791; afUserId=32ffe57f-53dd-4a0f-9e31-544ce94d96a6-p; IQ_userIdCookie=ES00251311611; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-582065-%22%2C%22at%22%3A%22ES00251311611%22%2C%22ac%22%3A%221%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; TestIfCookieP=ok; pbw=%24b%3d16970%3b%24o%3d11100%3b%24sw%3d1920%3b%24sh%3d1080; pid=239200228077632622; pdomid=22; _hjSessionUser_250321=eyJpZCI6ImFjMWQ1MDI5LTg2MTMtNTZiMS05NDNmLWI2MjUxNTI5NjE0MiIsImNyZWF0ZWQiOjE2NDM3OTM1ODA0NjEsImV4aXN0aW5nIjp0cnVlfQ==; smc="{}"; _cb_ls=1; _cb=CvBuo5Q84Kzf0Lmu; _chartbeat2=.1649232007164.1649232007164.1.Do9_KRdV-fZBkvjR0CTgWYAD4BH35.1; _gcl_au=1.1.1782543795.1652108343; atreman=%7B%22name%22%3A%22atreman%22%2C%22val%22%3A%7B%22camp%22%3A%22EPR-1151-%255Bexpress_alerts_20220608%255D-20220608-%255BProperty.LowPrice.Link%255D-72476654766%25401-20220608155557%22%2C%22date%22%3A459656.97373611113%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A2592000%2C%22end%22%3A2592000%7D%7D; lcsrd=2022-06-22T19:32:17.5076995Z; AF_SYNC=1655926337507; listingGalleryBoostEnabled=false; userUUID=c11b095c-8c9e-49ff-8673-dedf33031f8a; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7ImlkX3BhZ2VMYW5ndWFnZSI6ImVzIiwiaWRfdXNlclR5cGUiOiIxIn0sInVzZXJJZCI6IjI1MTMxMTYxMSJ9; send49890dc9-cf02-4526-a723-ea90481d2536="{\'friendsEmail\':null,\'email\':\'HG9JKRya00llZ60l6wbM5Yuwfh+wDFLMjZkCxwimZlI=\',\'message\':null}"; sasd2=q=%24qc%3D1308537863%3B%24ql%3DLow%3B%24qpc%3D07198%3B%24qt%3D228_3227_180861t%3B%24dma%3D0&c=1&l=1888570066&lo=993899153&lt=637921184624288094&o=1; sasd=%24qc%3D1308537863%3B%24ql%3DLow%3B%24qpc%3D07198%3B%24qt%3D228_3227_180861t%3B%24dma%3D0; askToSaveAlertPopUp=false; dyncdn=limit; uc="1XMwW8ZwehlN3QmXCDAo1Nphl0jT4xhiCqspR50+pG4noG9vvN9y/q8EQeqp1yCTY+sCrMm+mydyH/E42pRtSbA9qK/i8rKKohFsyBWXAJZia/hHnj6/Awxg6M7uTLIy/4vHDa0418c="; nl=1XMwW8ZwehlN3QmXCDAo1Nphl0jT4xhiCqspR50+pG4noG9vvN9y/q8EQeqp1yCTY+sCrMm+mydyH/E42pRtSbA9qK/i8rKKohFsyBWXAJZia/hHnj6/Ay5UT3lOJyow; SESSION=d7ab6b509870942b~2ac8f0d1-a048-4462-b106-67146052f3d0; cookieSearch-1="/venta-viviendas/palma-de-mallorca-balears-illes/:1656526335980"; contact2ac8f0d1-a048-4462-b106-67146052f3d0="{\'email\':\'HG9JKRya00llZ60l6wbM5Yuwfh+wDFLMjZkCxwimZlI=\',\'phone\':\'687261397\',\'phonePrefix\':\'34\',\'friendEmails\':null,\'name\':\'m8Czhnt6B3I=\',\'message\':null,\'message2Friends\':null,\'maxNumberContactsAllow\':10,\'defaultMessage\':true}"; ABTasty=uid=6qp48pmnq42mpgnx&fst=1643737775072&pst=1656520355499&cst=1656526337013&ns=30&pvt=1218&pvis=1&th=; ABTastySession=mrasn=&sen=0&lp=https%253A%252F%252Fwww.idealista.com%252Fventa-viviendas%252Fpalma-de-mallorca-balears-illes%252F; cc=eyJhbGciOiJIUzI1NiJ9.eyJjdCI6MzA2NzE1NjMsImV4cCI6MTY1NjYxMjczN30.qCzrbrlWdiPjU9Yrth6S_Q7RZarYYfyCrbyWeOEq4R4; cto_bundle=eHzPhl9zckg0JTJCWm9HYTZ5b0dISmJ4VnVRRGdjaDh2U2RJR0s4cTM2YkYwZ293YlFLbGhVczZYTXh6NkhwTDhMbG5CcjMlMkY1SWJiNk5TaGRYZkM0QkMwUWxmNE1GUG5wTjMlMkJ2UWlFUExtV2hQUTlvY0pPT2QwY0FHb0RnOGNOZGt0U2MlMkJjJTJCTFklMkJKJTJCVnhSUDRmMTByeHNqaGNpUSUzRCUzRA; _hjIncludedInSessionSample=0; _hjSession_250321=eyJpZCI6ImQ5N2RjZjIwLTIwMWEtNDhiYS1iM2FhLWE5YTU2OWM4ODg1ZiIsImNyZWF0ZWQiOjE2NTY1MjYzMzc0MDQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; datadome=AmJNsQWK8zyRFTIXv7SpIgEbEvt7tXH.xEMHutKlsNQ1X5~uTP8bGHlmXNds8KOGuqt2Yw63SEunVAijMbmd6v7n5dxmRrXUVtTuupGRxug9C59SAZL.6ukkgOqFSXf; utag_main=v_id:017e4d2c4ab4002313378430c37605072004406a00bd0$_sn:34$_se:1$_ss:1$_st:1656528136608$dc_visit:21$_prevCompletePageName:11%3A%3Alisting%3A%3AresultList%3A%3Aothers%3Bexp-1656529937035$_prevLevel2:11%3Bexp-1656529937035$_prevVtSource:directTraffic%3Bexp-1656527735322$_prevVtCampaignCode:%3Bexp-1656527735322$_prevVtDomainReferrer:%3Bexp-1656527735322$_prevVtSubdomaninReferrer:%3Bexp-1656527735322$_prevVtUrlReferrer:%3Bexp-1656527735322$_prevVtCampaignLinkName:%3Bexp-1656527735322$_prevVtCampaignName:%3Bexp-1656527735322$_prevVtRecommendationId:%3Bexp-1656527735322$ses_id:1656526336608%3Bexp-session$_pn:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:eu-central-1%3Bexp-session; vs=33114=4992132; cnfq=1; csfq=1')
    return req

#:scheme: https


# : ""
# : ?0
