import os

from robocorp.tasks import task
from RPA.Archive import Archive
from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP
from RPA.PDF import PDF
from RPA.Tables import Tables
from SeleniumLibrary.keywords import screenshot

ORDERS_URL = "https://robotsparebinindustries.com/orders.csv"
ORDERS_PATH = "./orders.csv"
ROBOT_ORDER_URL = "https://robotsparebinindustries.com/#/robot-order"
PDFS_FOLDER = "./output/pdfs"

browser = Selenium()
browser.headless = True
# browser.set_selenium_speed("0.1s")  # type:ignore
pdf = PDF()


@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    orders = get_orders()
    open_robot_order_website()

    for o in orders:
        close_annoying_modal()
        fill_the_form(o)
        click_preview()

        ordered = False
        while not ordered:
            click_order()
            ordered = browser.is_element_visible("id:order-another")

        store_receipt_as_pdf(o.get("Order number"))

        browser.click_button("id:order-another")  # type:ignore

    archive_receipts()


def get_orders():
    """Download orders.csv and return it as a table variable"""
    http = HTTP()
    tables = Tables()
    http.download(
        url=ORDERS_URL,
        target_file=ORDERS_PATH,
        overwrite=True,
    )

    return tables.read_table_from_csv(ORDERS_PATH)


def open_robot_order_website():
    browser.open_available_browser(ROBOT_ORDER_URL)


def close_annoying_modal():
    browser.click_button_when_visible(
        locator='xpath=//button[normalize-space(text())="OK"]'
    )


def fill_the_form(order: dict):
    browser.select_from_list_by_value("css:select#head", order.get("Head"))  # type: ignore
    browser.click_element(f'xpath=//input[@name="body" and @value="{order.get("Body")}"]')  # type: ignore
    browser.input_text('xpath=//input[@placeholder="Enter the part number for the legs"]', order.get("Legs"))  # type: ignore
    browser.input_text("id:address", order.get("Address"))  # type:ignore


def click_preview():
    browser.click_button("id:preview")  # type:ignore


def click_order():
    browser.click_button("id:order")  # type:ignore


def store_receipt_as_pdf(order_number):
    pdf_filename = f"robot_order_{order_number}.pdf"
    pdf_file = f"{PDFS_FOLDER}/{pdf_filename}"
    receipt_html = browser.get_element_attribute(
        "css:#receipt",  # type:ignore
        "outerHTML",
    )
    pdf.html_to_pdf(receipt_html, pdf_file)

    screenshot = screenshot_robot(order_number)
    embed_screenshot_to_receipt(screenshot, pdf_file)


def screenshot_robot(order_number):
    image_filepath = f"/tmp/robot_{order_number}.png"
    browser.capture_element_screenshot(
        "id:robot-preview-image",  # type:ignore
        image_filepath,
    )
    return image_filepath


def embed_screenshot_to_receipt(screenshot, pdf_file):
    pdf.add_watermark_image_to_pdf(
        image_path=screenshot,
        source_path=pdf_file,
        output_path=pdf_file,
    )


def archive_receipts():
    archive = Archive()
    archive.archive_folder_with_zip(
        folder=PDFS_FOLDER,
        archive_name="./output/pdfs.zip",
    )
