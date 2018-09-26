# Homework 1



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









### Reference

[1] Boutin, E., Ekanayake, J., Lin, W., Shi, B., Zhou, J., Qian, Z., Wu, M. and Zhou, L., 2014, October. Apollo: Scalable and Coordinated Scheduling for Cloud-Scale Computing. In *OSDI*(Vol. 14, pp. 285-300).

[2] Verma, A., Pedrosa, L., Korupolu, M., Oppenheimer, D., Tune, E. and Wilkes, J., 2015, April. Large-scale cluster management at Google with Borg. In *Proceedings of the Tenth European Conference on Computer Systems* (p. 18). ACM.

[3] Delgado, P., Dinu, F., Kermarrec, A.M. and Zwaenepoel, W., 2015. Hawk: Hybrid datacenter scheduling. In *Proceedings of the 2015 USENIX Annual Technical Conference* (No. CONF). USENIX Association.