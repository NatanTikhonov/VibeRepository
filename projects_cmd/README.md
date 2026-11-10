# projects_cmd — task_0 (Cmd)

Задания task_01-1, task_01-3 и task_01-4 написаны под Windows (CMD/PowerShell).
Я выполнял их на macOS в zsh, поэтому команды заменены аналогами:

| Windows | macOS (zsh) |
|---|---|
| `dir` / `Get-ChildItem` | `ls` |
| `HELP`, `cd /?` | `bash -c help`, `help cd` |
| `md` / `mkdir` | `mkdir` |
| `type` / `cat` | `cat` |
| `ren` | `mv` |
| `copy` / `Copy-Item` | `cp` |
| `Remove-Item` | `rm` |
| `tree /f` | `find . \| sort` |
| `notepad`, `Get-Process`, `Stop-Process` | `open -a TextEdit`, `pgrep`/`ps`, `pkill` |
| `Get-NetIPConfiguration` | `ipconfig getifaddr`, `netstat -rn` |
| `Test-Connection -Count 5` | `ping -c 5` |
| `$PSVersionTable` | `zsh --version`, `sw_vers` |
| `sfc /verifyonly` | `csrutil status` |

Вместо скриншотов `task_01_1-N.jpg` сохранены текстовые логи сеанса `task_01_1-N.txt`
(команда и её вывод).

- `task_01_1/` — задания 1–5 урока task_01-1
- `task_01_2/` — пустая папка по заданию 4
- `task_01_3/` — задания 1–4 и итоговый отчёт (`lab_final_report.txt`) уроков task_01-3 и task_01-4
