# Migri Appoinment Scheduler

It's usually quite hard to find a time slot for appointment in Migri so I created this script which monitors availability and shows a notification on Mac OS (other OSes not supported at the moment, but PRs are welcome). 

It's possible to configure some aspects of required appoinment directly in the script. For example it is possible to configure the number of people and the type of appointment for each as well as Migri office location.

# Installation

Create a new virtual environment

```bash
python -m venv ~/.local/share/virtualenvs/migri-appoinment-scheduler
. ~/.local/share/virtualenvs/migri-appoinment-scheduler/bin/activate
pip install -r requirements.txt
```

# Usage

```bash
Usage: main.py [OPTIONS]

Options:
  --office TEXT                   Migri office  [required]
  --reservation-type [permanent-residence-permit|family-first-and-extended-residence-permit|family-citizenship]
                                  Migri reservation type  [required]
  --min-date [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
                                  Earliest appoinment date  [required]
  --max-date [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
                                  Latest appoinment date  [required]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```

Example usage:

```bash
python main.py --office helsinki
               --reservation-type family-citizenship
               --min-date 2024-15-03
               --max-date 2021-15-07
```

In the example above we specify a reservation type for each person.

# Emailer setup
Instead of using macOS notification, you can setup SMTP emiler so the program will notify available slots to email. 
Create a file envs.py and enter the Google credentials for STMP setup. Note that you must create an app password to use Google SMTP server.