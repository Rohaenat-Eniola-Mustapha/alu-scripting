#!/usr/bin/env ruby

# Check if there is a single command-line argument (log entry)
if ARGV.length != 1
  puts "Usage: #{$0} '<log_entry>'"
  exit 1
end

# Get the log entry from the command line
log_entry = ARGV[0]

# Define regular expressions to extract sender, receiver, and flags
sender_pattern = /\[from:(.*?)\]/
receiver_pattern = /\[to:(.*?)\]/
flags_pattern = /\[flags:(.*?)\]/

# Use regular expressions to extract sender, receiver, and flags from the log entry
sender = log_entry.match(sender_pattern)[1]
receiver = log_entry.match(receiver_pattern)[1]
flags = log_entry.match(flags_pattern)[1]

# Output the extracted information in the required format
puts "#{sender},#{receiver},#{flags}"

