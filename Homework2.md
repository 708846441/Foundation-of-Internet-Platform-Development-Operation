# Homework 2



### 2. Network

#### 2.1. Local Area Network

Local area network, known as LAN,  is the most common network system. Typically, it has the following features

  - It has a rather small geological coverage, mostly within tens of kilometers.
  - It has higher transfer rate of information.
  - It is usually owned and operated by a private group or a person.

Generally, it also

- consists of cabling and one or more switches. A switch can be connected to a router, cable modem, or ADSL modem for internet access.
- can include a wide variety of devices such as firewalls, load balancers and network intrusion detection.

#### 2.2 . Internet Protocol Suite (TCP/IP)

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
 
#### 2.3. Domain Name System (DNS)
The Domain Name System (DNS) is a hierarchical decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It is used to translate human-friendly domain names into IP addresses, which are machine-friendly.
  ![DNS](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Domain_name_space.svg/600px-Domain_name_space.svg.png)

Users generally do not communicate directly with a DNS resolver. Instead DNS resolution takes place transparently in applications such as web browsers, e-mail clients, and other Internet applications. When an application makes a request that requires a domain name lookup, such programs send a resolution request to the DNS resolver in the local operating system, which in turn handles the communications required.

The DNS resolver will almost invariably have a cache (see above) containing recent lookups. If the cache can provide the answer to the request, the resolver will return the value in the cache to the program that made the request. If the cache does not contain the answer, the resolver will send the request to one or more designated DNS servers. 