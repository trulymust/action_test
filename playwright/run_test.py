# test_example.py
import pytest
import gspread
from playwright.sync_api import sync_playwright

# 测试环境搭建
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    # context.tracing.start(snapshots=True, sources=True, screenshots=True)
    yield context
    # context.tracing.stop(path="trace.zip")
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()

# 测试登录功能
def test_right_login(page):
    print('测试进行中')
    page.goto("https://www.baidu.com", timeout=0)
    page.locator("#kw").click()
    page.locator("#kw").fill("ceshii")
    page.get_by_role("button", name="百度一下").click()
    print(page.title())
    print('测试完成')

# 测试google表单填写模块
# def test_google_sheet(page):
#     # 进入Flow Builder模块
#     page.get_by_role("link", name="Flow Builder").click()
#     page.locator('//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/span/input').click()
    
#     page.get_by_label("Open").click()
#     page.get_by_role("option", name="Cnct Load Testing For Interview", exact=True).click()
#     page.get_by_role("button", name="Resend").click()

#     page.wait_for_timeout(10000)
#     # if(page.get_by_role("button", name="Confirm").is_visable()):
#     #     page.get_by_role("button", name="Confirm").click()
#     # 因网络原因导致的响应时间过长，加入强制等待
#     page.get_by_role("button", name="Continue").click()
#     page.get_by_role("button", name="Next").click()

#     # 打开Google Sheet填写号码
#     with page.expect_popup() as page1_info:
#         page.get_by_role("link", name="Add recipient list").click()
#     page1 = page1_info.value
#     gc = gspread.auth.oauth(credentials_filename='./credentials.json') # gspread授权

#     # 填写表格
#     sheet = gc.open_by_url(page1.url).get_worksheet(0)
#     line_tag = 2
#     for line in open('./books.txt', 'r', encoding='utf-8'):
#         print(line)
#         sheet.update_cell(line_tag, 1, line)
#         line_tag += 1

#     # 关闭弹出窗口
#     page1.close()
#     assert page.locator('//*[@id="root"]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/button').is_disabled() == False

# # 
# def test_submit(page):
#     # 验证信息并提交活动
#     page.get_by_role("button", name="Verify").click()
#     page.get_by_role("button", name="Next").click()
#     page.get_by_role("button", name="Submit Campaign").click()