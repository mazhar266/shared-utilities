#!/usr/bin/perl -w

# Watches till the domain gets Okay, shows a notification
# @author Mazhar Ahmed - CTO - Systech Unimax Limited
use Net::Ping;
                    
# check if the domain name is passed or not
if (!$ARGV [0]) {
    print "domain name is needed\n";
    die ();
}

# Host can be either an IP or domain name, get it from passed argument
my $host = $ARGV [0];
# Optionally specify a timeout in seconds (Defaults to 5 if not set)
my $timeout = 10;

# Create a new ping object
$p = Net::Ping->new ("icmp");

# Optionally specify a port number (Defaults to echo port is not used)
$p->port_number ("80");

# Perform the ping
$|++; # Ignore the buffer
while(!$p->ping ($host, $timeout)){
    print "$host is down.\n";
    sleep 1; # Retry after one second
}

# Print the result / success
print "Host ".$host." is alive\n";
# Send notification
# For Mac
system("osascript -e 'display notification \"$host is responding (timeout: $timeout)\" with title \"$host is Live\"'");
# For Ubuntu
system("notify-send \"$host is Live\" \"$host is responding (timeout: $timeout)\"");

# Close our ping handle
$p->close ();
