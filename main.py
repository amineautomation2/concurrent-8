import sys
import os
import time
from chelseafinancial import chelsea_runner
from halifax import halifax_runner
from iweb import iweb_runner
from quilter import quilter_runner
from standardlife import standard_life_runner
from willisowen import willis_owen_runner
from financial_discount import financial_discount_runner
from utils import get_random_user_agent, setup_driver, email_title
from charles_stanley import charles_stanley_runner
from interactive import interactive_runner
from hargreaves_lansdown import hl_runner


def main() -> None:
    start_time = time.perf_counter()
    headers = get_random_user_agent()
    driver = setup_driver(True)
    # chelsea_runner(headers)
    # halifax_runner(driver)
    # iweb_runner(driver)
    # quilter_runner(headers)
    # standard_life_runner(headers)
    # willis_owen_runner(headers)
    # financial_discount_runner()
    driver.quit()
    # with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    #    print(f"email_title={email_title()}", file=fh)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")


# if __name__ == "__main__":
#    main()


def run_scraper(platform: str):
    print(f"Starting scraper for: {platform}")
    match platform:
        # chelsea_financial, halifax, iweb, quilter, standard_life, willis_owen, financial_discount, financial_discount
        case "chelsea_financial":
            headers = get_random_user_agent()
            chelsea_runner(headers)
            return

        case "financial_discount":
            financial_discount_runner()
            return

        case "halifax":
            driver = setup_driver(True)
            halifax_runner(driver)
            driver.quit()
            return

        case "iweb":
            driver = setup_driver(True)
            iweb_runner(driver)
            driver.quit()
            return

        case "quilter":
            headers = get_random_user_agent()
            quilter_runner(headers)
            return

        case "standard_life":
            headers = get_random_user_agent()
            standard_life_runner(headers)
            return

        case "willis_owen":
            headers = get_random_user_agent()
            willis_owen_runner(headers)
            return

        case "charles_stanley":
            charles_stanley_runner()
            return

        case "interactive":
            interactive_runner()
            return

        case "hargreaves_lansdown":
            hl_runner()
            return


if __name__ == "__main__":
    # Get the platform name from the command line argument
    if len(sys.argv) > 1:
        target_platform = sys.argv[1]
        start_time = time.perf_counter()
        run_scraper(target_platform)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"[{target_platform}] Execution time: {elapsed_time:.2f} seconds")

    else:
        print("No platform specified!")
        sys.exit(1)
