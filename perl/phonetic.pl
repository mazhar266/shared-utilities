#!/usr/bin/perl -w

# check if the domain name is passed or not
if (!$ARGV [0]) {
    print "String is needed\n";
    die ();
}

# Sabre + Mr Mahabubur + Me Phonetic talks
my %letters;
# First digits
$letters{'0'} = 'Zero';
$letters{'1'} = 'One';
$letters{'2'} = 'Two';
$letters{'3'} = 'Three';
$letters{'4'} = 'Four';
$letters{'5'} = 'Five';
$letters{'6'} = 'Six';
$letters{'7'} = 'Seven';
$letters{'8'} = 'Eight';
$letters{'9'} = 'Nine';

# And now, letters
$letters{'A'} = 'Alpha';
$letters{'B'} = 'Bravo';
$letters{'C'} = 'Charlie';
$letters{'D'} = 'Delta';
$letters{'E'} = 'Echo';
$letters{'F'} = 'Fox';
$letters{'G'} = 'Golf';
$letters{'H'} = 'Harry';
$letters{'I'} = 'Item';
$letters{'J'} = 'Juliet';
$letters{'K'} = 'Kilo';
$letters{'L'} = 'Lima';
$letters{'M'} = 'Mike';
$letters{'N'} = 'Nancy';
$letters{'O'} = 'Oscar';
$letters{'P'} = 'Papa';
$letters{'Q'} = 'Queen';
$letters{'R'} = 'Romeo';
$letters{'S'} = 'Sugar';
$letters{'T'} = 'Tango';
$letters{'U'} = 'Union';
$letters{'V'} = 'Victor';
$letters{'W'} = 'William';
$letters{'X'} = 'X-Mas';
$letters{'Y'} = 'Yellow';
$letters{'Z'} = 'Zulu';

$string = $ARGV [0];
$string = uc $string;

for my $c (split //, $string) {
   print $letters{$c}, ' ';
}

print "\n";
