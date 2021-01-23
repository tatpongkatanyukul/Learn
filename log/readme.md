# Log of what I have done (usefully, or seemingly usefully of course)

## Jan 23rd, 2021

### file tags

The underlying motives are:
  * for building a searchable repository of programming problems

Examples, from MS Advanced Query Syntax, 
  * ```tags: (started AND python)``` for files having both tags "started" and "python"
  * ```tags: (started OR expression OR assignment)``` for files having tags "started", "expression" or "assignment"

![Get windows explorer to add tags to a file 1](https://github.com/tatpongkatanyukul/Learn/blob/main/log/tag000.png)
![Get windows explorer to add tags to a file 2](https://github.com/tatpongkatanyukul/Learn/blob/main/log/tag001.png)
![Get windows explorer to show tags](https://github.com/tatpongkatanyukul/Learn/blob/main/log/tag002.png)
![Get windows explorer to search for specific tags](https://github.com/tatpongkatanyukul/Learn/blob/main/log/tag003.png)

### Windows Command
from http://net-informations.com/q/mis/wmic.html#:~:text=WMIC%20is%20the%20abbreviation%20of,interfaces%20and%20through%20batch%20scripts.
  * Get system information
    * ```wmic computersystem get name, systemtype```
    * ```wmic computersystem get model```
    * ```wmic bios get serialnumber```
    * ```wmic nic get macaddress,description```
    * ```wmic baseboard get product,Manufacturer,version,serialnumber```
    * ```wmic COMPUTERSYSTEM get TotalPhysicalMemory```
    * ```wmic wmic process get workingsetsize,commandline```
    * ```wmic partition get name, size, type```
