# Homework 1

## Team members： 蔡一凡 李东起 姜凡叙 应邦豪

### 1. Introduction

The production clusters that we use for data-parallel computations are growing in size, each with over 20,000 servers. A growing community of thousands of users from many different organizations
submit jobs to the clusters every day, resulting in a peak rate of tens of thousands of scheduling requests per second. [1]

Each job consists of a number of tasks with cross-task dependencies. Here, we define that the task is a basic unit of computation that is scheduled to execute on a server.



### 2. Microsoft Apollo

#### 2.1. Characteristics

As is described in [1], Apollo has the following characteristics, 

 - Combines the distributed and coordinated concepts of design.
 - Matches jobs to resources
- Schedules each task on a server that minimizes the task completion time.
- Supplies individual schedulers with cluster information.
- Introduces opportunistic scheduling.
- Supports staged rollout to production clusters and validation at scale.



#### 2.2. Pros of Apollo

- It scales well without sacrificing scheduling quality.
- All schedulers are able to access the global status, therefore provide more accurate results.
- Self-correction mechanisms are implemented on all schedulers so that they can better schedule the resources.
- Is made robust through a series of correction and prediction mechanisms that dynamically adjust and rectify suboptimal decisions at runtime.
- Opportunistic scheduling in use to achieve high utilization while maintaining low job 



#### 2.3. Cons of Apollo

According to the description of [1], the following situations might happen, 

- Apollo schedules each task on a server that minimizes the task completion time. However, when there is a large number of simple tasks, it may take too much time on scheduling, while the tasks themselves only cost a little.
- The PN queue is mostly FIFO, but can be reordered. Therefore, there has to be a trade-off between starvation of some jobs and re-arrangement time cost.
- To handle a higher task arriving rate, Apollo's distributed and coordinated system might not be able to handle high dimensional resources as centralized systems do. [2]
- Apollo does not differentiate between long and short jobs and uses the same mechanisms to schedule both types of jobs. [3]



#### 2.4. Our Comments

Unlike Borg and some other scheduling systems, Apollo uses a combination of distributed and coordinated system to balance the latency and utilization, which is an innovation. It also uses opportunistic execution mechanism and self correction and prediction to better schedule the tasks in runtime. However, the distributed structure does have its drawbacks. It is not so good as dealing with high dimensional resources, and the communications between nodes can cost some time. Moreover, the jobs are neither estimated nor scheduled at arriving time, the correction of which might be a cause of waste of resource.



### 3. Google Borg

#### 3.1. Characteristics

As is described in [2], Borg has the following characteristics, 

 - It achieves high utilization by combining admission control, efficient task-packing, over-commitment, and machine sharing with process-level performance isolation.
 - It supports high-availability applications with runtime features that minimize fault-recovery time, and scheduling policies that reduce the probability of correlated failures.
-  Borg simplifies life for its users by offering a declarative job specification language, name service integration, real-time job monitoring, and tools to analyze and simulate system behavior.



#### 3.2. Pros of Borg

- Allocs are useful.
- Cluster management is more than task management.
- Introspection is vital.
- The master is the kernel of a distributed system.



#### 3.3. Cons of Borg



- Jobs are restrictive as the only grouping mechanism for tasks.
- One IP address per machine complicates things.
- Optimizing for power users at the expense of casual ones.



#### 3.4. Our Comments

Borg provides three main benefits: it 
- hides the details of resource management and failure handling so its users can focus on application development instead; 
- operates with very high reliability and availability, and supports applications that do the same; 
- lets us run workloads across tens of thousands of machines effectively. 

Borg is not the first system to address these issues, but it’s one of the few operating at this scale, with this degree of resiliency and completeness.


### 4. Alibaba Sigma

#### 4.1. Characteristics

*Sigma* is a container dispatching system within the scope of Alibaba Group. It successfully supports the extremely large number of transaction during the purchases at China's Double Eleven Day. 

As an successful underlying infrastructure for Alibaba's operation and maintenance systems, Sigma is famously known to be:

- providing effective online cluster management and online resource scheduling
- utilizing advantages of Container concepts, so that resources are optimally isolated and safe, reducing costs of operation and maintenance 
- suitably and preferably placed in mixed architectures where online services and offline processing run in parallel, significantly improving CPU resource utilization with no increase in response time
- after more than 2 years of trial demonstration, structural adjustment and  optimization, already gone into mass production
- strongly compatible, hoping to combine the power of ecology for joint construction and development

#### 4.2.  Pros of Sigma

- *Sigma* has three-layers with clear division of labor: *Alikenel*, *SigmaSlave* and *SigmaMaster*. 
    * *Alikenel* is deployed on Physical machine to improve kernel algorithms in task scheduling. 
    * *SigmaSlave* is responsible for CPU resources allocation in container, so it tends to quickly make trade-offs between new-coming delay-sensitive and insensitive tasks. 
    * *SigmaMaster* is the dominant pillar, optimizing resource scheduling allocation.

   These layers gives finer controll on task priority. It can also generate different strategies on different stages. Don't worry about whether these layers coordinates badly. Kernel resource isolation techniques promises that final consistency of the system is very satisfactory.

- *Sigma* is supportive in mixed architectures. As imagined, machines that process online requests usually have low CPU utilization (because of the disorder of requests and the implicit but ultimate needs to keep their orders synchronized). While *Sigma* is compatible with Fuxi, an offline resource scheduling system, making it possible to deploy different tasks to the same batch of machines to ensure that utilization of physical machine resources is saturated.

- *Sigma* benefits from *PouchContainer*'s containerization that gives great isolation, compatibility and safety. To today, *PouchContainer* already makes online business reach 100% containerization, and computing tasks also begin to containerize.

- *Sigma* passed through the tests specially designed for it. Alibaba made a schedule simulator named *Cetebro* for developement of *Sigma*, which produces highly customized 1:1 environment data.


#### 4.3. Cons of Sigma



- Although passed millions of tests, *Sigma* still needs to be observed in real mass production environment.

- All the tests now are static. Therefore, scientists still need to implement the idealized orthogonal dynamic simulation tools to do some trials for complementation, and promote the development of scheduling algorithms.


#### 4.4. Our Comments

*Sigma* is in 'Chinese style', just like Chinese ticketing systems, it is borned to cope with suprising amount of transaction that is only possible to be realistic in China. Fortunately, *Sigma* is proved to be successful and open source for scientists de go deeper into related knowledge.

### 5. Google Omega

#### 5.1 Characteristics

As is described in [5], Omega has the following characteristics, 

- Presents a lightweight taxonomy of the option space for cluster scheduler development.

- Builds a parallel scheduler architecture around shared state. Each scheduler can access to the entire cluster, and is allowed to compete in a free-for-all manner.

- Uses lock-free optimistic concurrency control to mediate clashes when scheduler updates the cluster state.


#### 5.2 Pros of Omega

- Omega shared-state architecture can deliver performance competitive with or superior to other architectures, and that interference in real-world settings is low.
- Omega has the ability to access the entire cluster state in a scheduler.
- Omega greatly increases the performance of the scheduler and has better utilization.
- The utilization ratio of hardware is high, which make full use of the resources.



#### 5.3 Cons of Omega

- For it doesn't exist central resource allocator in Omega, it's hard to achieve an fair scheduling. One scheduler may get the resources it needs more quickly, and may be more likely to race to control resources that are supposed to be distributed to others.
- As a result of the Multi-Version Concurrency Control, there may be more conflicts during Omega runs. Solving these conflicts requires extra works. The more conflicts appear, the more quickly the performance decreases.
- Omega has great requirements for configuration for tolerance.



#### 5.4 Our Comments

What Google requires is a scheduler architecture that can accommodate both types of jobs, flexibly support job-specific policies, and also scale to an ever-growing amount of scheduling work. Therefore, Google brings up Omega to replace Mesos. As is said in the paper, Omega balances its pros and cons quite well, and it performs well during these years.

### Reference

[1] Boutin, E., Ekanayake, J., Lin, W., Shi, B., Zhou, J., Qian, Z., Wu, M. and Zhou, L., 2014, October. Apollo: Scalable and Coordinated Scheduling for Cloud-Scale Computing. In *OSDI*(Vol. 14, pp. 285-300).

[2] Verma, A., Pedrosa, L., Korupolu, M., Oppenheimer, D., Tune, E. and Wilkes, J., 2015, April. Large-scale cluster management at Google with Borg. In *Proceedings of the Tenth European Conference on Computer Systems* (p. 18). ACM.

[3] Delgado, P., Dinu, F., Kermarrec, A.M. and Zwaenepoel, W., 2015. Hawk: Hybrid datacenter scheduling. In *Proceedings of the 2015 USENIX Annual Technical Conference* (No. CONF). USENIX Association.

[4] 阿里系统软件技术, 2018, June. 阿里巴巴 Sigma 调度和集群管理系统架构详解. In
*51CTO Blog 2.0*.

[5] Schwarzkopf, M., Konwinski, A., Abd-El-Malek, M., & Wilkes, J. (2013).*Omega: flexible, scalable schedulers for large compute clusters*. ACM.