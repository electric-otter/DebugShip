# Setting up variables
$x = 10
$y = 20

# Set breakpoints on variables to pause execution when they are accessed or changed
Set-PSBreakpoint -Variable x
Set-PSBreakpoint -Variable y

# Perform the calculation
$z = $x + $y

# Output the result
Write-Output $z

# Optionally, wait for debugger to attach or pause manually for debugging
Wait-Debugger

# Assume you are invoking an external debugger command targeting a device
$targetDevice = "device_id"  # Replace with the actual target device
$options = "--option value"  # Replace with the actual options for your debugger

# Construct the command string
$debugger = "debugger --target $targetDevice $options $PSBoundParameters $Args Set-PSBreakPoint"


Invoke-Expression $debugger
