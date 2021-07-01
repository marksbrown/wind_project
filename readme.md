# Project - Weather
Started : 30th June 2021

# Summary
This repo contains the code for analysing storm information data provided.

## Data Format
“20100720-0722 CHANTHU\WP CCH\cch00720.w1a”
“20100720-0722 CHANTHU”: 2010 is the year, 0720-0722 is the range of dates in mmdd form,
CHANTHU is the storm name
“WP CCH”: WP is the instrument type, here Wind Profiler. CCH is the station name.
“cch00720.w1a”: cch is again the station name, 00720 is the data in ymmdd form. w is the type of
data, here wind. 1 is the mode of the wind profiler, here is low mode. ‘a’ is the stage of processing.
You’ll probably only be using wind profiler data in this project so for now, you can focus only on data
in the WP* folders. Other storms have different instrument types available.
The data type can be ‘w’ wind or ‘t’ temperature. You’ll only need ‘w’ wind.
Regarding the ‘mode’. It can take values of 1 or 3. Mode 1 has the best boundary layer resolution
and is limited to about 1600 m. Mode 3 goes up to about 5000m or higher but has lower vertical
resolution. You can probably focus exclusively on mode 1, but bear in mind mode 3 may also have
useful data and may fill some of the gaps in mode 1.
The final character ‘a’ or ‘b’ reflects that stage of post-processing. There is generally very little
difference between them except in ‘b’ there are more samples flagged as suspicious in the QC. You
should stick to one or the other, ‘b’ is safest as it has the stricter QC.
Regarding your general strategy. I don’t think you should limit your analysis to one station (e.g. CCH)
but rather aim to build the most complete data set for all the storms you can. Cross-comparison
between stations may be an interesting validation but not the main focus.
Ralf mentioned that height bins will be useful when combining your data. Using a similar idea with
time maybe helpful too. E.g. averaging within 1 hr bins maybe a useful method to get a more
complete and regular dataset.
