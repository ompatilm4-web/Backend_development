import requests
import bs4


def scrape_jobs(keyword="python"):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}"

    jobs_list = []

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            print("Request Failed:", response.status_code)
            return jobs_list

        soup = bs4.BeautifulSoup(
            response.text,
            'html.parser'
        )

        job_cards = soup.find_all(
            'div',
            class_='base-search-card'
        )

        for job in job_cards:

            title_tag = job.find('h3')

            company_tag = job.find('h4')

            location_tag = job.find(
                'span',
                class_='job-search-card__location'
            )

            link_tag = job.find('a')

            jobs_list.append({

                "title": (
                    title_tag.get_text(strip=True)
                    if title_tag else "N/A"
                ),

                "company": (
                    company_tag.get_text(strip=True)
                    if company_tag else "N/A"
                ),

                "location": (
                    location_tag.get_text(strip=True)
                    if location_tag else "N/A"
                ),

                "link": (
                    link_tag['href']
                    if link_tag and link_tag.has_attr('href')
                    else "#"
                )
            })

    except Exception as e:
        print("SCRAPING ERROR:", e)

    return jobs_list