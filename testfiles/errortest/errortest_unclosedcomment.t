# this is an unclosed comment, should raise an error in the parser step
$include[std]
$entry main
proc main() -> void:
    std.out("Hello, World!")
    end