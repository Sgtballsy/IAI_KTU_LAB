start:-
    hypothesis(Disease),
    write("I believe you have: "),nl,
    write(Disease),nl,
    write("Take Care!!"),
    undo.

/* test them hypothesis*/

hypothesis(covid) :- covid, ! .
hypothesis(cold) :- cold, ! .
hypothesis(measles) :- measles, ! .
hypothesis(unknown) . /* no diagnosis */

/* rules for identification */

covid :-
    check(fever),
    check(dry_cough),
    check(shortness_of_breath),
    write("Advices and Suggestions: "),nl,
    write("Quarantine for Two Weeks."),nl.

cold :-
    check(headache),
    check(runny_nose),
    check(sneezing),
    check(sore_throat),
    write("Advices and Suggestions: "),nl,
    write("1. Tylenol Tablet"),nl,
    write("2. Panadol Tablet"),nl,
    write("3. Nasal Spray"),nl,
    write("4. Wear Warm clothes."),nl.

measles :-
    check(fever),
    check(runny_nose),
    check(rash),
    check(conjunctivitis),
    write("Advices and Suggestios: "),nl,
    write("1. Acetaminophen Tablet"),nl,
    write("2. Advil Tablet"),nl,
    write("3. Aleve Tablet"),nl,
    write("4. please isolate yourself!!"),nl.

ask(Question) :-
    write("Does the patient have following symptoms?"),nl,
    write(Question),
    read(Response),nl,
    (   (   Response==yes;Response==y)
    ->
    assert(yes(Question));
    assert(no(Question)),fail).
:- dynamic yes/1,no/1.

check(S) :-
    (   yes(S)
    ->
    true;
    ( no(S)
    ->
    fail;
    )
    )
undo ;- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.
