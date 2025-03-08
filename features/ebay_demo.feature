Feature: SauceDemo Website Functionality
    @tc-ebay-1
    Scenario: Access a Product via category after applying multiple filters
        Given I am on the eBay homepage
        When I navigate to "Electronics" category
        When I navigate to "Cell Phones & Accessories" subcategory
        When I navigate to "Cell Phones & Smartphones" subcategory
        And I apply the following filters "Condition" with "New"
        And I apply the following filters "Storage Capacity" with "128 GB"
        And I apply the following filters "Brand" with "Sony"
        Then I should see all selected "3 filters applied"

    @tc-ebay-2
    Scenario: Access a Product via Search
        Given I am on the eBay homepage
        When I enter "MacBook" in the search bar
        And I select "Computers/Tablets & Networking" from the search category
        Then the first result name should contain "MacBook"
        