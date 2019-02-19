#!/usr/bin/env perl6

use v6;

my @lines = "../data-representation/database-IT-EN-GER-USDA-GRE.md".IO.lines;

my @names = @lines.grep( /^^ \s* \| \s+ \d+ \s+ \|/ );

my %present;
for @lines -> $l {
    my $name = $l.split("|")[2];
    my $checks = ($l ~~ m:g/\| \s+ x/).elems;
    %present{$checks}.push: $name;
}

say "$_ checks → ", %present{$_}.join(", ") for <4 5>;

