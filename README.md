<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
-->



<!-- PROJECT LOGO -->
<br />
<div align="right">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://cdn.dribbble.com/users/2463018/screenshots/13930887/f1_mclaren_final-05.jpg" alt="Logo" width="160" height="160">
  </a>

<h3 align="center">Formula 1 Data ETL/ELT Pipeline</h3>

  <p align="center">
    This project utilises modern data stack etl/elt technologies such as Terraform, DBT and Snowflake, to ingest, transform and deploy real-word formula 1 data from a source postgres database to a full fledged snowflake datawarehouses, in which data can be further transformed to meet end-users needs (with DBT)
    <br />
    <a href="https://github.com/formula1elt"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This projet uses data downloaded from the ergast api documentation: http://ergast.com/mrd/.
The API provides data for the Formula One series, from the beginning of the world championships in 1950. I have downloaded four database tables containing these results i.e the Circuits, Races, Constructors and Results tables, and have stored the tables within four respective schemas of a postgres database hosted by Airflow.
The aim of this project is to extract the data from these source postrges tables, load the corresponding files to an S3 datalake (using Airflow), further extract to a snowflake database staging area (using Airflow) and finally to the datawarehouse layer of the snowflake database where DBT will be utilised to carry out necessary transformations. Terraform will be used to provision required resources for the project, such as IAM roles and S3 buckets.


### Built With

[![Te,o][Temi.js]][Next-url] [![React][React.js]][React-url][![Vue][Vue.js]][Vue-url] [![Angular][Angular.io]][Angular-url][![Svelte][Svelte.dev]][Svelte-url][![Laravel][Laravel.com]][Laravel-url][![Bootstrap][Bootstrap.com]][Bootstrap-url]


<img src="https://media.giphy.com/media/ObNTw8Uzwy6KQ/giphy.gif" width="30px">&nbsp;***Languages & Tools I Know...***
<p align="left">
  
  https://download.logo.wine/logo/PostgreSQL/PostgreSQL-Logo.wine.svg
  <code><img height="50" src="https://download.logo.wine/logo/PostgreSQL/PostgreSQL-Logo.wine.svg"></code><code> 
  <img height="50" src="https://github.com/uannabi/-/blob/master/resource/dj.svg"> </code>
  <code> <img height="50" src="https://github.com/uannabi/-/blob/master/resource/jp.svg"> </code>
  <code> <img height="50" src="https://github.com/uannabi/-/blob/master/resource/docker-ar21.svg"> </code>
  <code> <img height="50" src="https://github.com/uannabi/-/blob/master/resource/git.svg"> </code>
  <code> <img height="50" src="https://github.com/uannabi/-/blob/master/resource/linux-ar21.svg"> </code>
  <code> <img height="50" src="https://github.com/uannabi/-/blob/master/resource/other/apache_hadoop-ar21.svg"> </code>
  <code> <img height="50" src="https://github.com/uannabi/-/blob/master/resource/other/mongodb-ar21.svg"> </code>
  <code> <img height="50" src="https://github.com/uannabi/-/blob/master/resource/other/sqlite-ar21.svg"> </code>
  <code> <img height="50" src="https://github.com/uannabi/-/blob/master/resource/other/mysql-ar21.svg"> </code>
  <code> <img height="50" src="https://github.com/uannabi/-/blob/master/resource/other/postgresql-ar21.svg"> </code>
  <code> <img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg"> </code>
  <code> <img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg"> </code>
  <code> <img height="50" src="https://github.com/Akash-chowrasia/Akash-chowrasia/blob/main/images/flask.svg"> </code>
  <code> <img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg"> </code>
  <code> <img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg"> </code>
  <code> <img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg"> </code>
  <code> <img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg"> </code>
  <code> <img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg"> </code>
  <code> <img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sass/sass-original.svg"> </code>
  <code> <img height="50" src="  https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg
"> </code>
  <hr>
  <p align="center">

<p align="right">



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
