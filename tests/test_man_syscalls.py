import sys
sys.path.append('../src/utils')

from ManScrapper import ManScrapper

def test_get_syscalls_man_page():
    scrap = ManScrapper("http://man7.org/linux/man-pages/man2/syscalls.2.html")
    syscalls = scrap.getManPage();
    assert syscalls.status_code == 200
    assert 'syscalls' in syscalls.name

