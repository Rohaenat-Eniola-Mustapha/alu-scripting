#!/usr/bin/env ruby

# Check if there is a single command-line argument
if ARGV.length != 1
  puts "Usage: #{$0} <string>"
  exit 1
end

# Get the argument from the command line
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /hbtn\d{4}/

# Check if the input string matches the regular expression
if input_string =~ pattern
  puts input_string
else
  puts "$"
end

