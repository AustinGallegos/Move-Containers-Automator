import managers as m
from webdrivers import chrome_driver as cd


def main():
    totes = m.read_totes("txt/totes.txt")

    driver, wait = cd.setup_driver()
    m.sign_in(driver)
    m.goto_app(driver, wait)

    for tote in totes:
        m.move_tote(driver, wait, tote.strip(), "tsXX")
        m.move_tote(driver, wait, "tsXX", tote.strip())

    driver.quit()


if __name__ == "__main__":
    main()
