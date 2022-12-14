from urllib.parse import urlparse
import streamlit as st
from scraper import Scraper, gen_usn, roll_range


class ExamScraper(Scraper):
    def __init__(self, url="https://exam.msrit.edu/"):
        self.URL = url + ("/" if url[-1] != "/" else "")
        super(ExamScraper, self).__init__()

    def get_post_body(self, payload):
        soup = self.get_soap(self.URL, "POST", payload)
        body = soup.body
        try:
            _ = body.find_all("h3")[0].text
            return body
        except IndexError:
            return

    def get_stats(self, payload) -> dict[str, str]:
        body = self.get_post_body(payload)
        if body is None: return {}
        url = urlparse(self.URL)
        return {
            "usn": payload["usn"],
            "name": body.find_all("h3")[0].text,
            "sgpa": body.find_all("p")[3].text,
            "photo": f"{url[0]}://{url[1]}" + body.find_all("img")[1]['src'],
        }

    def get_dept(self, head: str, year: str, dept: str, tolerate: int = 5):
        payload = gen_payload()
        tol = tolerate
        if tol <= 0: return
        payload["usn"] = gen_usn(year, dept, roll, head)
        stats = self.get_stats(payload)
        if not stats:
            tol -= 1
        tol = tolerate
        yield stats


def gen_payload() -> dict[str, str]:
    return {
        "usn": "",
        "osolCatchaTxt": "",
        "osolCatchaTxtInst": "0",
        "option": "com_examresult",
        "task": "getResult"
    }


def micro(head: str, year: str, dept: str, rollnum):
    with ExamScraper("https://exam.msrit.edu/eresultseven/") as EXAM:
        for stat in EXAM.get_dept(head, year, dept, rollnum):
            write = \
                f"{stat['usn']:{len(head + year + dept) + 3 + 5}}," \
                f"{stat['name']:64}," \
                f"{stat['sgpa']:5}," \
                f"{stat['photo']}," \
                f""
            print(write)
            profile_image = f"{stat['photo']}"
            st.image(profile_image, caption=stat['name'], use_column_width=True)
            st.subheader(f'CGPA: {stat["sgpa"]}')


if __name__ == '__main__':
    HEAD = "1MS"
    st.title("Find Anyone's CGPA just using USN")
    usn = st.text_input("Enter your USN")
    check = False
    if len(usn) == 10:
        check = True
    btn = st.button("Check CGPA")
    if check or btn:
        roll = int(usn[7:10])
        DEPT = usn[5:7].upper()
        YEAR = usn[3:5]
        micro(HEAD, YEAR, DEPT, roll)
