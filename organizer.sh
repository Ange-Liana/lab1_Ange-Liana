#!/bin/bash

# make sure the archive folder exists
if [ ! -d "archive" ]; then
  mkdir archive
fi

# generate a timestamp to uniquely rename files
timestamp=$(date +"%Y%m%d-%H%M%S")

# check if the grades file exists before trying to move it
if [ -f "grades.csv" ]; then
  newname="grades_$timestamp.csv"
  
  # move the file into the archive folder with the new name
  mv grades.csv archive/$newname
  
  # create a fresh empty file for new data
  touch grades.csv
  
  # record what just happened into the log file
  echo "$timestamp - grades.csv archived as $newname" >> organizer.log
else
  # log the case where the file was missing
  echo "$timestamp - grades.csv not found" >> organizer.log
fi
