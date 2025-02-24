# Standard Python Libraries
from datetime import datetime, timedelta
import os
import sys

# Third-Party Libraries
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Third-Party Libraries
from utils.qualys_api_search.search_scans import search_scans
from utils.qualys_api_search.search_schedules import search_schedules


def test_search_scans(monkeypatch):
    no_scans = datetime.utcnow() + timedelta(hours=4)
    no_scans = no_scans.strftime("%Y-%m-%dT%H:%M:%SZ")
    monkeypatch.setattr("utils.qualys_api_search.search_scans.INPUT_DATE", no_scans)
    with pytest.raises(SystemExit) as excinfo:
        stakeholders = search_schedules()
        search_scans(stakeholders)

    assert excinfo.value.code == "ERROR: No scans found. Review dailywas.log for query"
    print("No scans found scenario was handled properly")


if __name__ == "__main__":
    pytest.main()
