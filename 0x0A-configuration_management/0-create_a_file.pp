# Create a file

file {'/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet'
}