# DevOpsPractical
# QA Devops Practical Project

First Commit  

## Project Brief:

This is a simple Dev Ops project to show the linking of microservices and automation between them. 

## Project Technolgies;
##### Aim to be used and Included
*Jira  for Kanban Boards and Project Management
*Git for Version Control
*Jenkins for Continuous Intregation
*Ansible for configuration management/automation
*GCP as cloud platfrom to host services
*Docker for Containerisation and Swarm Orchestration
*NGINX for Reverse Proxy 


## App Focus

Housing Prices Monitor for those looking at buying a home. 
Users should be able to select the house Hocations and size of House they are looking for and be able to get rough prices based on those factors.

*Service1 - Database 
*Service2 - FrontEnd
*Service3 - Houses Locations
*Service4 - House Size
*Service5 - House Prices Estimate


## Project Management
#### Planning, and Design: Jira 

I am trying out Jira as the service/tool for my project management for this project. Jira is similar to trello and is a good way to track a projects progress, keep track of tasks within a team, as well upload documents and keep commentary of challenges/issues.

**See Jira Image in Images Folder**


## Database Entity Diagram

Image needs to be created.

## Risk assessment

Still needs to be made.


## Overall Service Architecture

The plan was to use all the services, however i am yet to include a swarm or ansible succesfully in the project. However the next steps would be to include these, and quite possibly to use ansible to create the docker swarm.  The rest of the services follow this route up to the deployment phase. Credits to Earl Gray for the grpahic. 

**See Service Architecture and pipeline in Images Folder**

## Pipeline

Pipeline was primarly done through Jenkins by making a pipeline project. There is a script called jenkinsfile which contains the order and instructions that jenkins follows for its pipeline. The jenkins images shows a succesfuly completed build via this pipeline. Jenkins also webhooks any updates from the github repo for live updates and new builds.

## Example Service Progress

See Image Service Structure & Python of Service2

## Testing



## The future
Immediate next steps would be Swarm depoyment through ansible.
Further Development of the application would be utilising full CRUD to allow the user to choose what house type they want to generate the price for. As well as displaying DB history. And Fancier development of webpage html rather than basic output. 

Acknowledgements:
All trainers at QA. Leon, Adam and Earl for support for this project.
As as well as team for advice/bug fixing.
