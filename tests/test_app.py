from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

def test_get_posts(page, test_web_address, db_connection):
    db_connection.seed("seeds/post_user.sql")
    page.goto(f"http://{test_web_address}/home")
    page.screenshot(path="screenshot.png", full_page=True)
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
    "Author: Guest published on: 2022-12-08 13:45:21 Smoking so much I cant breathe",
    "Author: bob_gratton published on: 2022-02-08 18:45:21 Am i really all the things that are outside of me",
    "Author: Guest published on: 2021-12-09 15:45:21 There are pinguins on the beach",
    ])

def test_create_user(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/post_user.sql")
    page.goto(f"http://{test_web_address}/home")
    page.click("text=Sign up to Chitter")
    page.fill("input[name=name]", "Test name")
    page.fill("input[name=email]", "allo@gmail.com")
    page.fill("input[name=username]", "Test username")
    page.fill("input[name=password]", "123456")
    page.click("text='Create Account'")

def test_create_post(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/post_user.sql")
    page.goto(f"http://{test_web_address}/home")
    page.fill("input[name=content]", "Test the new peep content")
    page.click("text='Post Peep'")

    content_element = page.locator(".t-content")
    expect(content_element).to_have_text(["Test the new peep content",
                                        "Smoking so much I cant breathe",
                                        "Am i really all the things that are outside of me",
                                        "There are pinguins on the beach"])
    

def test_login(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/post_user.sql")
    page.goto(f"http://{test_web_address}/home")
    page.click("text=Login to Chitter")
    page.fill("input[name=email]", "allo@gmail.com")
    page.fill("input[name=password]", "123456")
    page.click("text='Log In'")