if [ $# -eq 0 ]
then
	echo "Inavolid no "
	exit
else
	for login in $*
	do
		if grep $login /etc/passwd > /dev/null
		then
			echo "Login login: $login"
			dir=`grep $login /etc/passwd|cut -d ":" -f6`
			echo "Home directory is : $dir"
		fi
	done
fi
