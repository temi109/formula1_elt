
<a name="readme-top"></a>
<!--

-->



<!-- PROJECT SHIELDS -->
<!--
-->



<!-- PROJECT LOGO -->
<br />
<div align="right">
  <a href="https://github.com/temi109/formula1_elt.git">
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

<!-- PROJECT SHIELDS -->



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
This project uses data downloaded from the ergast api documentation: http://ergast.com/mrd/.
The API provides data for the Formula One series, from the beginning of the world championships in 1950. I have downloaded four database tables containing these results i.e the Circuits, Races, Constructors and Results tables, and have stored the tables within four respective schemas of a postgres database hosted by Airflow.
The aim of this project is to extract the data from these source postrges tables, load the corresponding files to an S3 datalake (using Airflow), further extract to a snowflake database staging area (using Airflow) and finally to the data warehouse layer of the snowflake database where DBT will be utilised to carry out necessary transformations. Terraform will be used to provision required resources for the project, such as IAM roles and S3 buckets.



### Built With


<img src="https://media.giphy.com/media/ObNTw8Uzwy6KQ/giphy.gif" width="30px">&nbsp;***Languages & Tools I Know...***
<p align="left">
  
<code><img height="50" src="images/Snowflake_Logo.svg.png"></code> <code><img height="50" src="images/airflow_log.png"></code> <code><img height="50" src="images/aws_s3.png"> </code><code> <img height="50" src="images/dbt_logo.png"> </code><code> <img height="50" src="images/postgres_logo.png"></code> <code><img height="50" src="images/terraform_logo.png"></code>



<!-- GETTING STARTED -->

### Prerequisites

* Postgres Database
* AWS Account
* Terraform installed
* DBT installed

#### Required for KinD Cluster:

- Kubectl
- Helm
- Docker
- KinD


To initialise terraform and create the s3 bucket, run the following commands:

```sh

  terraform init  
  
  terraform validate

  terraform plan

  terraform apply

  ```



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<img height="500" width="750" border="10" src="images/trial workflow.png">

### Installation

1. Clone the repo
 ```sh
 https://github.com/temi109/formula1_elt.git
 ```
2. Change directories into k8s-airflow folder and create a k8s cluster of 1 control plane and 3 worker nodes
 ```sh
 cd k8s-airflow/

 kind create cluster --name airflow-cluster --config kind-cluster.yaml

 # Add the official repository of the Airflow Helm Chart
 helm repo add apache-airflow https://airflow.apache.org

 # Update the repo
 helm repo update

 # Create namespace airflow
 kubectl create namespace airflow

 # Check the namespace 
 kubectl get namespaces

 # Install the Airflow Helm Chart and start it 
 helm install airflow ./airflow/ --namespace airflow --debug

 # Get pods
 kubectl get pods -n airflow
 ```
3. Build dockerfile and upgrade the cluster
 ```sh

 # (Make sure you're in k8s-airflow folder)
 docker build -t airflow-custom:2.5.1 .

 kind load docker-image airflow-custom:2.5.1 --name airflow-cluster

 cd airflow/

 helm upgrade airflow --values=myvalues.yaml . --namespace airflow --debug

 # Port forward 8080:8080
 kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow --context kind-airflow-cluster

 # Validating server up and running
 Go to browser and type localhost:8080 into browser search, and the username/password admin, admin respectively.

 ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_





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
