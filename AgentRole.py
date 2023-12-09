from enum import Enum


class AgentRole(Enum):
    RESEARCHER = 1,
    BUSINESS_ANALYST = 2,
    ARCHITECT = 3,
    DEVELOPER = 4,
    TESTER_UNIT = 5,
    TESTER_INTEGRATION = 6,
    TESTER_UI = 7,
    QA_CODE_REVIEWER = 8,
    PUBLISHER_INTERNAL = 9,
    PUBLISHER_PUBLIC = 10
