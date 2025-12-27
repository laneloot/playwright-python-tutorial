from playwright.sync_api import expect, Page

def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo home page is displayed
    page.goto('https://www.duckduckgo.com')

    print('before')

    # When the user searches for a phrase
    page.locator('#searchbox_input').fill('panda')
    page.locator('button.iconButton_button__A_Uiu.searchbox_searchButton__LxebD').click()

    # Then the search result query is the phrase
    expect(page.locator('#search_form_input')).to_have_value('panda')

    # And the search result links pertain to the phrase
    page.locator('a[data-testid="result-title-a"]').nth(4).wait_for()
    titles = page.locator('a[data-testid="result-title-a"]').all_text_contents()
    print('titles')
    print(titles)
    matches = [t for t in titles if 'panda' in t.lower()]
    assert len(matches) > 0

    expect(page).to_have_title('panda at DuckDuckGo')