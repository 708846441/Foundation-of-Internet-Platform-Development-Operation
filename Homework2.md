# Homework 2

## 1. Storage(Ceph)

 As is described in [1], Ceph directly addresses the issue of scalability while simultaneously achieving high performance, reliability and availability through three fundamental design features: 
 
  - decoupled data and metadata
  - dynamic distributed metadata management
  - reliable autonomic distributed object storage

### 1.1. Decoupled Data and Metadata

Ceph maximizes the separation of ﬁle metadata management from the storage of ﬁle data. Metadata operations (open, rename, etc.) are collectively managed by a metadata server cluster, while clients interact directly with OSDs to perform ﬁle I/O (reads and writes). Object-based storage has long promised to improve the scalability of ﬁle systems by delegating low-level block allocation decisions to individual devices. 

- However, in contrast to existing object-based ﬁlesystems [2,3,4,5] which replace long per-ﬁle block lists with shorter object lists, Ceph eliminates allocation lists entirely. 
- Instead, ﬁle data is striped onto predictably named objects,while a special-purpose data distribution function called CRUSH [6] assigns objects to storage devices. 

This allows any party to calculate (rather than look up) the name and location of objects comprising a ﬁle’s contents,eliminating the need to maintain and distribute object lists, simplifying the design of the system, and reducing the metadata cluster workload.

### 1.2. Dynamic Distributed Metadata Management

Because ﬁle system metadata operations make up as much as half of typical ﬁle system workloads [7], effective metadata management is critical to overall system performance. Ceph utilizes a novel metadata cluster architecture based on Dynamic Subtree Partitioning [8] that adaptively and intelligently distributes responsibility for managing the ﬁle system directory hierarchy among tens or even hundreds of MDSs. 

A (dynamic) hierarchical partition preserves locality in each MDS’s workload, facilitating efﬁcient updates and aggressive prefetching to improve performance for common workloads. Signiﬁcantly, the workload distribution among metadata servers is based entirely on current access patterns, allowing Ceph to effectively utilize available MDS resources underany workload and achieve near-linear scaling in the number of MDSs.
 
### 1.3. Reliable Autonomic Distributed Object Storage

Large systems composed of many thousands of devices are inherently dynamic: they are built incrementally,they grow and contract as new storage is deployed and old devices are decommissioned, device failures are frequent and expected, and large volumes of data are created, moved, and deleted. All of these factors require that the distribution of data evolve to effectively utilize available resources and maintain the desired level of data replication. 

Ceph delegates responsibility for data migration, replication, failure detection, and failure recovery to the cluster of OSDs that store the data, while at a high level, OSDs collectively provide a single logical object store to clients and metadata servers. This approach allows Ceph to more effectively leverage the intelligence (CPU and memory) present on each OSD to achieve reliable, highly available object storage with linear scaling.

## 2. Network

### 2.1. Local Area Network

Local area network, known as LAN,  is the most common network system. Typically, it has the following features

  - It has a rather small geological coverage, mostly within tens of kilometers.
  - It has higher transfer rate of information.
  - It is usually owned and operated by a private group or a person.

Generally, it also

- consists of cabling and one or more switches. A switch can be connected to a router, cable modem, or ADSL modem for internet access.
- can include a wide variety of devices such as firewalls, load balancers and network intrusion detection.

### 2.2. Internet Protocol Suite (TCP/IP)

The Internet protocol suite provides end-to-end data communication specifying how data should be packetized, addressed, transmitted, routed and received.

This functionality is organized into four abstraction layers, which classify all related protocols according to the scope of networking involved. From lowest to highest, the layers are

- the link layer, containing communication methods for data that remains within a single network segment (link).

- the internet layer, providing internetworking between independent networks

- the transport layer, handling host-to-host communication.

- the application layer, providing process-to-process data exchange for applications.

  ![Four layers and their usage](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/UDP_encapsulation.svg/700px-UDP_encapsulation.svg.png)

There is another widely used protocol known as UDP, and here are the major differences between TCP and UDP.

 <table>
 <thead>
 <tr>
<td></td> <th>TCP</th> <th>UDP</th>
 </tr> 
 </thead>

<tbody>
 <tr>
 <th> Connection	</th>
 <td> A connection-oriented protocol</td>
 <td> A connectionless protocol</td>
 </tr>

 <tr>
 <th> Ordering of data</th>
 <td> Rearranges data packets in the order specified.</td>
 <td> Has no inherent order as all packets are independent of each other. If ordering is required, it has to be managed by the application layer.</td>
 </tr>

 <tr>
 <th>Reliability</th>
 <td>There is absolute guarantee that the data transferred remains intact and arrives in the same order in which it was sent.
 </td>
 <td>
 There is no guarantee that the messages or packets sent would reach at all.
 </td>
 </tr>

 <tr>
 <th>Weight</th>
 <td>TCP is heavy-weight. TCP requires three packets to set up a socket connection, before any user data can be sent. TCP handles reliability and congestion control.
 </td>
 <td>
 UDP is lightweight. There is no ordering of messages, no tracking connections, etc. It is a small transport layer designed on top of IP.
 </td>
 </tr>

 <tr>
 <th>Usage</th>
 <td>TCP is suited for applications that require high reliability, and transmission time is relatively less critical.
 </td>
 <td>
UDP is suitable for applications that need fast, efficient transmission, such as games. UDP's stateless nature is also useful for servers that answer small queries from huge numbers of clients.
 </td>
 </tr>


 </tbody>
 </table>
 
### 2.3. Domain Name System (DNS)

The Domain Name System (DNS) is a hierarchical decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It is used to translate human-friendly domain names into IP addresses, which are machine-friendly.

  ![DNS](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Domain_name_space.svg/600px-Domain_name_space.svg.png)

Users generally do not communicate directly with a DNS resolver. Instead DNS resolution takes place transparently in applications such as web browsers, e-mail clients, and other Internet applications. When an application makes a request that requires a domain name lookup, such programs send a resolution request to the DNS resolver in the local operating system, which in turn handles the communications required.

The DNS resolver will almost invariably have a cache (see above) containing recent lookups. If the cache can provide the answer to the request, the resolver will return the value in the cache to the program that made the request. If the cache does not contain the answer, the resolver will send the request to one or more designated DNS servers. 

## Reference

[1] S. Weil, S. Brandt, E. Miller, D. Long, C. Maltzahn, "Ceph: A Scalable High-Performance Distributed File System", Proc. of the 7th Symposium on Operating Systems Design and Implementation, November 2006.

[2] P. J. Braam. The Lustre storage architecture. http://www.lustre.org/documentation.html, Cluster File Systems, Inc., Aug. 2004. 

[3] S. Ghemawat, H. Gobioff, and S.-T. Leung. The Google ﬁle system. In Proceedings of the 19th ACM Symposium on Operating Systems Principles (SOSP ’03), Bolton Landing, NY, Oct. 2003. ACM. 

[4] G. A. Gibson, D. F. Nagle, K. Amiri, J. Butler, F. W. Chang, H. Gobioff, C. Hardin, E. Riedel, D. Rochberg, and J. Zelenka. A cost-effective, high-bandwidth storage architecture. In Proceedings of the 8th International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS),pages 92– 103, San Jose, CA, Oct. 1998.

[5] B. Welch and G. Gibson. Managing scalability in object storage systems for HPC Linux clusters. In Proceedings of the 21st IEEE / 12th NASA Goddard Conference on Mass Storage Systems and Technologies, pages 433–445, Apr. 2004. 

[6] S. A. Weil, S. A. Brandt, E. L. Miller, and C. Maltzahn. CRUSH: Controlled, scalable, decentralized placement ofreplicateddata. InProceedingsofthe2006 ACM/IEEE Conference on Supercomputing (SC ’06), Tampa, FL, Nov. 2006. ACM. 

[7] D. Roselli, J. Lorch, and T. Anderson. A comparison of ﬁle system workloads. In Proceedings of the 2000 USENIXAnnualTechnicalConference, pages41–54, San Diego, CA, June 2000. USENIX Association.

[8] S. A. Weil, K. T. Pollack, S. A. Brandt, and E. L. Miller. Dynamic metadata management for petabyte-scale ﬁle systems. In Proceedings of the 2004 ACM/IEEE Conference on Supercomputing (SC ’04). ACM, Nov. 2004. 

