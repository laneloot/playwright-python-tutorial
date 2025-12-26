from playwright.sync_api import Page

def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo home page is displayed
    page.goto('https://www.duckduckgo.com')

    # When the user searches for a phrase
    page.locator('#searchbox_input').fill('panda')
    page.locator('button.iconButton_button__A_Uiu.searchbox_searchButton__LxebD').click()

    # Then the search result query is the phrase
    # And the search result links pertain to the phrase
    # And the search result title contains the phrase
    pass