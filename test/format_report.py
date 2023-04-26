import re
from datetime import datetime, timezone, timedelta

def escape_ansi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)

markdown_with_ansi = ""
with open("report.md",'r') as my_file:
      markdown_with_ansi = my_file.read()
md_without_ansi = "# Result\n\n" + escape_ansi(line = markdown_with_ansi)
tz = timezone(timedelta(hours=+8))
now = datetime.now(tz)
date_and_time = "\n### Test time\n\nReport generated on " + str(now.strftime("%Y-%m-%d at %H:%M:%S")) + "\n"
md_plus_time = md_without_ansi + date_and_time
with open("report.md",'w') as my_file:
      my_file.write(md_plus_time)