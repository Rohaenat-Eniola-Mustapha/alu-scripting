#!/usr/bin/env ruby

# Check if there is a single command-line argument
if ARGV.length != 1
  puts "Usage: #{$0} <string>"
  exit 1
end

# Get the argument from the command line
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /./

# Initialize an empty result string to store matches
result = ""

# Use the scan method to find all matches and concatenate them
input_string.scan(pattern) { |match| result += match }

# Print the result
puts result

