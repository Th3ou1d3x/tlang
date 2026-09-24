$include[std] # include from INSIDE the binary ## $ = compiler flag #
# $import[std] include from OUTSIDE the binary #
$entry main
proc main() -> void:
    std.out("Hello, World!")