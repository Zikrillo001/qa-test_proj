from src.core.base_page import BasePage


class ProductsPage(BasePage):
    PRODUCTS_LINK = "a[href='/products']"
    PRODUCT_NAMES = ".productinfo p"  # product name textlar ko'pincha shu yerda

    def open_products(self):
        self.page.click(self.PRODUCTS_LINK)
        self.page.wait_for_load_state("domcontentloaded")

    def get_first_product_names(self, limit: int = 5) -> list[str]:
        items = self.page.locator(self.PRODUCT_NAMES)
        count = min(items.count(), limit)
        names = []
        for i in range(count):
            txt = items.nth(i).inner_text().strip()
            if txt:
                names.append(txt)
        return names
