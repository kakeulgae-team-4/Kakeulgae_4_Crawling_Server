from typing import List, Optional
from datetime import datetime


class AfterProcessDto:
    __company_name: str
    __post_name: str
    __career: List[str]  # ['신입', '경력']
    __education: str
    __region_1st: str
    __region_2nd: str
    __work_type: str
    __job_detail: List[str]
    __deadline: Optional[datetime]  # 2024-03-21
    __url: str
    __created_at: datetime  # 어제 -> 2024-03-10

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name):
        self.__company_name = company_name

    @property
    def post_name(self):
        return self.__post_name

    @post_name.setter
    def post_name(self, post_name):
        self.__post_name = post_name

    @property
    def career(self):
        return self.__career

    @career.setter
    def career(self, career):
        self.__career = career

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, education):
        self.__education = education

    @property
    def region_1st(self):
        return self.__region_1st

    @region_1st.setter
    def region_1st(self, region_1st):
        self.__region_1st = region_1st

    @property
    def region_2nd(self):
        return self.__region_2nd

    @region_2nd.setter
    def region_2nd(self, region_2nd):
        self.__region_2nd = region_2nd

    @property
    def work_type(self):
        return self.__work_type

    @work_type.setter
    def work_type(self, work_type):
        self.__work_type = work_type

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline):
        self.__deadline = deadline

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at
