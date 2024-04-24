<p align="center">
  <img src="https://ichef.bbci.co.uk/images/ic/1200x675/p0h4mqdq.jpg" width="200" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">Projet INF8808</h1>
</p>
<p align="center">
    <em><code>CAF - Africa Cup of Nations</code></em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=default&logo=pandas&logoColor=white" alt="Pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=default&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=default&logo=Plotly&logoColor=white" alt="Plotly">
	<img src="https://img.shields.io/badge/Dash-008DE4.svg?style=default&logo=Dash&logoColor=white" alt="Dash">
	<img src="https://img.shields.io/badge/Gunicorn-499848.svg?style=default&logo=Gunicorn&logoColor=white" alt="Gunicorn">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=default&logo=Flask&logoColor=white" alt="Flask">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Main goals](#-main-goals)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

The Africa Cup of Nations is a football sports event organized every two years by the Confederation of African Football. In 2023, this event brought together 24 teams from the African continent, pre-selected for the final phases. The competition took place in January 2024, but it was designated as the 2023 Africa Cup of Nations. SportsAI, a Canadian company specialized in sports data visualization, with whom we are collaborating on this project, has provided us with access to various statistics on the matches that took place. We will present these statistics in the following sections of this introductory report.

---

##  Main goals

How to explain Ivory Coast's victory? What are the criteria explaining the superiority of this team in the context of the Africa Cup of Nations? These two questions involve different sub-goals: characterizing the teams in the competition, analyzing the journey of each team, and identifying their strengths and weaknesses. The general goal of our visualization is to easily compare teams based on performance criteria, which we will determine in collaboration with SportsAI.

---

##  Repository Structure

```sh
└── ./
    ├── Code
    │   ├── app.py
    │   ├── app_init.py
    │   ├── init_pretraitement.py
    │   ├── methodologie.py
    │   ├── visu1.py
    │   ├── visu1_pretraitement.py
    │   ├── visu2.py
    │   ├── visu2_pretraitement.py
    │   ├── visu3.py
    │   ├── visu3_pretraitement.py
    │   ├── visu4.py
    │   └── visu4_pretraitement.py
    ├── Data
    │   ├── delete_first_letters_csv.py
    │   ├── graph
    │   ├── graph_distribution.py
    │   ├── projet_data_1.csv
    │   ├── projet_data_1.xlsx
    │   ├── projet_data_2.csv
    │   ├── projet_data_2.xlsx
    │   ├── projet_data_3.csv
    │   ├── projet_data_3.xlsx
    │   ├── projet_data_4.csv
    │   └── projet_data_4.xlsx
    ├── requirements.txt
    └── server.py
```

---

##  Modules

<details open><summary>.</summary>

| File                                 | Summary                         |
| ---                                  | ---                             |
| [server.py](server.py)               | <code>This Python script contains a Flask server to run a web application using Dash, with a failsafe mechanism implemented.</code> |
| [requirements.txt](requirements.txt) | <code>Requirements to install before execution</code> |

</details>

<details open><summary>Code</summary>

| File                                                  | Summary                         |
| ---                                                   | ---                             |
| [app.py](Code/app.py)                                 | <code>Overall construction of the application</code> |
| [app_init.py](Code/app_init.py)                       | <code>Opening of the application</code> |
| [init_pretraitement.py](Code/init_pretraitement.py)   | <code>Preprocessing for the dropdown menu</code> |
| [visu1_pretraitement.py](Code/visu1_pretraitement.py) | <code>Preprocessing for the first visualization</code> |
| [visu1.py](Code/visu1.py)                             | <code>Construction of the first visualization</code> |
| [visu2_pretraitement.py](Code/visu2_pretraitement.py) | <code>Preprocessing for the second visualization</code> |
| [visu2.py](Code/visu2.py)                             | <code>Construction of the second visualization</code> |
| [visu3_pretraitement.py](Code/visu3_pretraitement.py) | <code>Preprocessing for the third visualization</code> |
| [visu3.py](Code/visu3.py)                             | <code>Construction of the third visualization</code> |
| [visu4_pretraitement.py](Code/visu4_pretraitement.py) | <code>Preprocessing for the fourth visualization</code> |
| [visu4.py](Code/visu4.py)                             | <code>Construction of the fourth visualization</code> |
| [methodologie.py](Code/methodologie.py)               | <code>Construction of the methodology page</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the INF8808_Projet repository:
>
> ```console
> $ git clone https://github.com/gillonlo/INF8808_Projet.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd INF8808_Projet
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run server using the command below:
> ```console
> $ python server.py
> ```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/gillonlo/INF8808_Projet/issues)**: Submit bugs found or log feature requests for the `.` project.
- **[Submit Pull Requests](https://github.com/gillonlo/INF8808_Projet/pulls)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your local account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone ../.
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to local**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com/gillonlo/INF8808_Projet/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=">
   </a>
</p>
</details>

---

##  License

This project is protected under the GNU AGPLv3 License. For more details, refer to the [LICENSE](https://github.com/gillonlo/INF8808_Projet/blob/main/license.txt) file.

---

##  Acknowledgments

- Théau Lepouttre, Marouane Oudada, Louis Gillon, Carrie Kam, Laurène Ralay, Laure-Anne Réau

[**Return**](#-overview)

---
