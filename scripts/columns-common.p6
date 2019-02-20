#!/usr/bin/env perl6

use v6;

my %classed = "../data-representation/database-IT-EN-GER-USDA-GRE.md".IO.lines.grep( /^^ \s* \| \s+ \d+ \s+ \|/ ).classify( { ($_ ~~ m:g/\| \s+ x/).elems } );

say "$_ checks → ", %classed{$_}.map( *.split("|")[2] ).join(", ") for <3 4 5>;

