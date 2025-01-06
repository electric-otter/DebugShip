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
# Make the options for target devices or 
$options = "$targetDevice $ForEach-Object"
# Construct the command string
$debugger = "debugger --target $targetDevice $options $PSBoundParameters $Args Set-PSBreakPoint $procInfo"


Invoke-Expression $debugger
