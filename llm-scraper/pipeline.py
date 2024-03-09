import requests
from prefect import flow, task
from prefect.server.schemas.schedules import IntervalSchedule

import scraper.indeed_scraper as indeed_scraper

# Below is the flow that should can be called (after you define it it)

# scrape_and_load_positions(positions = ["data engineer", "analytics engineer"], 
# locations=["New York City", "San Francisco"], pages = 5
# )


# And below is the deployment, and how to schedule this 
# if __name__ == "__main__":
#     scrape_and_load_positions.serve(
#         name="scrape-and-load-deployment",
#         schedule=IntervalSchedule(interval=100),
#         parameters={'positions': ["data engineer", "analytics engineer"], 
#         'locations': ["New York City", "San Francisco"], "pages": 5}
#         )
