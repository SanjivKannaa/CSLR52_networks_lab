set ns [new Simulator]
set nf [open mesh.nam w]
$ns namtrace-all $nf
set tf [open mesh.tr w]
$ns trace-all $tf
proc finish {} {
global ns nf tf
$ns flush-trace
close $nf
close $tf
# exec nam mesh.nam &
# exit 0
}
set N [lindex $argv 0]
set PACKETSIZE [lindex $argv 1]
for {set i 0} {$i < $N} {incr i} {
set n($i) [$ns node]
}
for {set i 0} {$i < $N} {incr i} {
for {set j 0} {$j < $N} {incr j} {
if { $i!=$j} {
$ns duplex-link $n($i) $n($j) 10Mb 10ms DropTail
}
}
}
for {set i 0} {$i < $N} {incr i} {
if {$i % 2 != 0} {
# create udp agent
set udp($i) [new Agent/UDP]
$ns attach-agent $n($i) $udp($i)
# create a cbr traffic
set cbr($i) [new Application/Traffic/CBR]
$cbr($i) set packetSize_ $PACKETSIZE
$cbr($i) set interval_ 0.005
$cbr($i) attach-agent $udp($i)
} else {
set null($i) [new Agent/Null]
$ns attach-agent $n($i) $null($i)
}
}
for {set i 1} {$i < $N} {set i [expr {$i + 2}]} {
for {set j 0} {$j < $N} {set j [expr {$j + 2}]} {
$ns connect $udp($i) $null($j)
$ns at 0.0 "$cbr($i) start"
$ns at 100.0 "$cbr($i) stop"
}
}
$ns at 100.0 "finish"
$ns run