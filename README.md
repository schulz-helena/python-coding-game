# python-programmierkurs
Ein Kurs, der Kindern / Teenagern spielerisch beibringen soll, wie das Programmieren in Python funktioniert.
Es werden Labyrinth-Level bereitgestellt, in denen ein markiertes Ziel erreicht werden soll.
Dabei steuern die TeilnehmerInnen den Spieler mit ihrem selbstgeschriebenen Code.
Begleitend gibt es eine PowerPoint-Präsentation, in der wir vor jeder Phase ein neues Programmier-Konzept erklären.
Diese Präsentation enthält außerdem eine Musterlösung für alle Level.


## Phasen
### Phase 1 (level1_x)
Wir starten mit einer Einführung in einige der von uns bereitgestellten Funktionen, mit denen der Spieler sich in den Leveln fortbewegen kann.
Die Level sind simpel aufgebaut und lassen sich durch die Aneinanderreihung weniger Movement-Befehle lösen.
Hier sollen die TeilnehmerInnen sehen, wie sich das Aufrufen der Funktionen in Bewegungen des Spielers überträgt. 

### Phase 2 (level2_x)
In dieser Phase erklären wir das Konzept einer For-Schleife.
Die TeilnehmerInnen sollen bestenfalls feststellen, dass die Lösungen der Level aus dieser Phase sehr lang werden würden, wenn man jeden einzelnen Funktionsaufruf ausschreiben müsste (z.B. 10 Mal hintereinander move()).
In einem späteren Level dieser Phase können auch geschachtelte Schleifen verwendet werden, um die Lösung noch kürzer zu machen.

### Phase 3 (level3_x)
Hier erklären wir zunächst While-Schleifen und wie sie sich von For-Schleifen unterscheiden.
Wir stellen zudem eine neue Funktion bereit, die diesmal keine Movement-Funktion ist, sondern überprüft, ob das Ziel bereits erreicht ist und damit einen Wahrheitswert zurückgibt.
Die TeilnehmerInnen sollen ein paar der bereits aus Phase 2 bekannten Labyrinthe lösen und sehen, dass mit der Verwendung von While nicht vorab festgelegt werden muss, wie oft ein bestimmtes Muster ausgeführt werden soll. 

### Phase 4 (level4_x)
Zunächst erklären wir, wie ein If-Else-Block funktioniert.
Wir ergänzen den Funktions-Pool um eine Funktion, die zurückgibt, ob sich der Spieler im nächsten Schritt forwärts bewegen kann, oder ob eine Wand ihn blockiert.
Die Level in dieser Phase lassen sich nun nicht mehr durch das Wiederholen eines bestimmten Musters lösen.
Stattdessen müssen Fallunterscheidungen angewendet werden, um zum Ziel zu gelangen.

### Phase 5 & weitere
Hier wollen wir Level bereitstellen, die Münzen enthalten, welche aufgesammelt werden müssen.
Außerdem wollen wir das Konzept von Listen erklären und einbringen, z.B. so dass gesammelte Münzen einer Liste hinzugefügt werden sollen und das Level nur als geschafft gilt, wenn die Liste alle Münzen enthält.
...