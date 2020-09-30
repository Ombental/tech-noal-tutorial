from pathlib import Path
from typing import Dict, List, Union
import os
import requests
import time


PATH_TO_SITES = 'sites.txt'
REQUEST_AMOUNT = 100


def requester(site_url: str) -> Dict[str, str]:
    timer = [time.perf_counter()]
    log = ''
    for i in range(REQUEST_AMOUNT):
        response = requests.get(site_url)
        if response:
            timer.append(time.perf_counter())
        else:
            log += f'Request number {i + 1} failed with error code {response.status_code}\n'
    log += f'Total Failed Requests: {REQUEST_AMOUNT - len(timer) + 1}'
    median = (timer[-1] - timer[0]) / (len(timer) - 1)
    if len(timer) > 2:
        mean = timer[(len(timer) - 1) // 2] - timer[(len(timer) - 1) // 2 - 1]
    return {'mean': str(mean), 'median': str(median),'log': log,'url': site_url}


def html_output(path: Path, sites_info: List[Dict[str, str]]) -> None:
    html = """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8"/>
            <title>Requests Report</title>
        </head>
        <body>
            <dl>""" # headers and all
    for site in sites_info:
        html += f"""
        <dt><h2>INFO FOR REQUESTS TO <a href="{site['url']}">{site['url'].upper()}</a></h2></dt>
            <dd>Median request time: {site['median']} seconds</dd>
            <dd>Mean request time: {site['mean']} seconds</dd><br><br>
            <dd>Log Info:<br>{site['log']}</dd>
        
        """
    html += """
            </dl>
        </body>
    </html>"""
    with path.open('w') as f:
        f.write(html)


def file_output(path: Path, sites_info: List[Dict[str, str]]) -> None:
    with path.open('w') as f:    
        for site in sites_info:
            f.write('*' * 100)
            f.write(f"\nINFO FOR REQUESTS TO {site['url'].upper()}\nMedian request time: {site['median']} sec\nMean request time:{site['mean']} sec\n\nLog info:\n{site['log']}")


def prints_to_printer(path: Path) -> None:
    os.startfile(path, "print")


if __name__ == "__main__":
    path = Path(PATH_TO_SITES)
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"{PATH_TO_SITES} doesn't point to a legitimate file")
    sites_info = []
    with path.open(mode='r') as f:
        for line in f:
            sites_info.append(requester(line.strip()))
    file_output(path.parent / 'output.txt', sites_info)
    html_output(path.parent / 'output.html', sites_info)
    prints_to_printer(path.parent / 'output.txt')
    
