# Hi Corbett, Donald, and Greg,

I hope you are doing well. Thank you for submitting your project proposal. We enjoyed reviewing the proposal video and slides. We are providing your feedback and grade in this email (see below).

Thank you,  
Professor Ahmed & DGMD17 Staff

---

## Proposal Feedback:

### Scope: 15 pts
**Feedback:** Great project scope on brass collection. The motivation and impact are clear, and the final results are communicated well. It is also great the idea is something that one of you can personally relate to and would solve a problem you face currently.

### Timeline: 25 pts
**Feedback:** Great timeline and great job factoring in time for important project parts (such as writing the report and consolidating everything). Based on the technology stack you are using, we've found groups in the past typically need more time than what's described in your project proposal. We recommend prioritizing, timeboxing, and/or planning in more buffer. More detailed feedback below.

### Technologies / Methods: 25 pts
**Feedback:** The two main components for this project are: hardware and simulation. Each are both pretty involved with their own subcomponents. For the hardware, there's 3D printing, a Roomba, a Raspberry Pi, and a LiDAR sensor, each of which can be pretty involved. Controlling a Roomba is quite difficult as there is no official API. In the past, projects that used a Roomba didn't attempt to control it but used its default pathing to collect data and list out what decisions they would instruct a robot to make based on the data feed. We'd recommend timeboxing the Roomba control aspect to avoid sinking too much time into something that perhaps may not be very customizable. As for the Raspberry Pi and LiDAR, that is more feasible and can be set up so that the Pi is storing the data on device (on an SD card) or sends the signals to your computer via Bluetooth. As for 3D printing, it seems like a group member has significant experience in it so there's less concern of this taking up too much time. For the hardware aspect, we recommend following the example project (Deep See) where they used a default Roomba, attached the LiDAR sensor with a Raspberry Pi, and simulate an environment (for them, they used cups to represent obstacles, for your team, it would be 3D printed brass).

As for the software stack, there is ROS, Gazebo, and SLAM, which are all pretty involved. ROS/Gazebo is an industry standard, but has a learning curve to them. In the past, projects that used these tools ended up spending a lot of time learning and not implementing, so we recommend using something lighter weight, especially if the end goal is to use a SLAM algorithm and not run full simulations. If the goal is, however, to use ROS/Gazebo, we recommend spending most of the project on learning this and then implementing your simulation.

### Division of Labor: 25 pts
**Feedback:** Clear division of labor as stated in the slides. The division appears to work in parallel.

### References: 3 pts
**Feedback:** Links to source/relevant technologies are listed, but missing links to existing work/brass collection solution.

### Format: 5 pts
**Feedback:** Great presentation design and every person spoke.

### Overall: 98 pts
**Feedback:** Overall, this is a great project proposal. The idea is very relevant and solves a real-world problem. Our biggest point of feedback is the technology stack and timeline is very ambitious and can take quite a lot of time to ramp on. As a result, we recommend simplifying some of the steps.

One option is to focus on hardware, data collection, and decision simulation. In this approach, you'd use the default Roomba setting, attach sensors on top that collect data which are stored or transmitted via Bluetooth, and 3D-printed brass items that the sensors will detect. Once you collect the data, you'd simulate the decision process (i.e., what would the robot do in this scenario if you could control the robot). The deliverable would be the robot (which would be communicated via a video), the data collected, and a program that takes in data and gives us decisions. The division of labor would mostly stay the same.

An alternative project path is to focus on learning ROS and Gazebo and using simulation. The end result here would be a simulation of brass on the ground and a robot collecting them via SLAM algorithms. The main focus would be learning the tool and then making a very thorough simulation. The division of labor would be that everyone learns ROS and Gazebo and that different people work different simulation scenarios or different aspects of the same simulation.

Whichever decision your team decides, do let us know (email us) and we can set the project expectation accordingly.
