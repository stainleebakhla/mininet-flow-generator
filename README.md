# Mininet Flow Generator

This is a custom python script to run Mininet. This script has the ability to generate random flows between hosts, for the controller to detect and classify.

## Getting Started

These instructions will help you install and setup Mininet Flow Generator into your local machine for development and testing purposes.

### Prerequisites

This script requires Mininet to be installed in the system.

### Installing

Simply clone this repository for installing it into your local computer.

```
git clone https://github.com/stainleebakhla/mininet-flow-generator.git
```

## Running Mininet Flow Generator

The following command will run this script

```
python topo_launcher.py
```

If the script is already made executable then we can simply run the script as

```
./topo_launcher.py
```

The available command line arguments are as follows:

1. `--controller=remote[,ip=<ip_address>]`: This argument starts Mininet with a remote controller for our SDN network. The location of the controller can be specified with `ip_address`. If no IP address is specified, then it is assumed that the
controller is running locally, and the value `localhost` is assumed. If this argument
is not supplied, then Mininet starts it own default controller instead.

2. `--topo=<topo_name>[,nodes]`: This argument specifies the topology with which Mininet should start with. Available values are `linear`, `mesh` and `fat_tree` topologies. The `nodes` specify the number of nodes to be spawned in that particular topology. If not specified, it assumes the value of 2. If this argument is not specified, then it assumes the value of linear topology with 2 nodes.

3. `--debug`: If specified, this argument starts the python script in debug mode. It tries to connect to a locally available PyCharm IDE. If not specified, the script starts normally without opening any debug ports.

Once Mininet is started, it shows up the following prompt

```
GEN/CLI/QUIT>_
```

Here it shows there are three commands available. The description of the three commands are as follows:

1. `GEN`: This is the main purpose of the script. This command generates flows between two hosts randomly selected. This command takes 3 inputs, experiment time, no of elephant flows and no of mice flows, and creates a schedule of those many elephant and mice flows selected at random and then executes them using `iperf`. For each flow, two random hosts from the network are selected, one is selected as a server, the other is selected as a client. The server command is run at the host selected as the server, and the client command is run at the host selected as client. This generates a traffic flow between two nodes in the network, which is picked up by ONOS for analysis. Once the flows have been generated, the script goes to sleep for the remaining duration of the experiment, so as to not disturb any of the ongoing flows. At the end of the experiment, the script starts up the cleaning process, by removing all the server and client `iperf` processes it had started. If in case there are any existing flows that is flowing, these are stopped and killed immediately. However care has been taken such that all flows generated with this command terminates well before the duration of the experiment.

2. `CLI`: This command starts the Mininet CLI. Here you can enter commands, which is run by Mininet.

3. `QUIT`: The command exits the script so started, shutting down Mininet and all the components, like switches, and links that it had started.
