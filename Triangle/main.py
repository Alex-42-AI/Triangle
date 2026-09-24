import tkinter as tk

from tkinter import ttk, messagebox

from solver import solve

INPUT_FIELDS = [
    ("a", "Side a"),
    ("b", "Side b"),
    ("c", "Side c"),
    ("A", "Angle A (°)"),
    ("B", "Angle B (°)"),
    ("C", "Angle C (°)"),
    ("h_a", "Height h_a"),
    ("h_b", "Height h_b"),
    ("h_c", "Height h_c"),
]

OUTPUT_FIELDS = [
    ("a", "Side a"),
    ("b", "Side b"),
    ("c", "Side c"),
    ("A", "Angle A (°)"),
    ("B", "Angle B (°)"),
    ("C", "Angle C (°)"),
    ("h_a", "Height h_a"),
    ("h_b", "Height h_b"),
    ("h_c", "Height h_c"),
    ("P", "Perimeter"),
    ("S", "Area"),
    ("m_a", "Median a"),
    ("m_b", "Median b"),
    ("m_c", "Median c"),
    ("b_a", "Bisector a"),
    ("b_b", "Bisector b"),
    ("b_c", "Bisector c"),
    ("R", "Circumradius"),
    ("r", "Inradius"),
]


class TriangleGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Triangle Calculator")
        self.root.geometry("900x650")
        self.root.resizable(False, False)
        self.input_vars = {}
        self.output_vars = [{}, {}]
        self.status = None
        self.build_ui()

    def build_ui(self):
        title = ttk.Label(
            self.root,
            text="Triangle Calculator",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(pady=10)

        main = ttk.Frame(self.root)
        main.pack(fill="both", expand=True, padx=15, pady=10)

        left = ttk.Frame(main)
        left.pack(side="left", fill="y")

        right = ttk.Frame(main)
        right.pack(side="right", fill="both", expand=True)

        self.build_inputs(left)
        self.build_outputs(right)
        self.build_buttons()

        self.status = ttk.Label(
            self.root,
            text="Ready.",
            anchor="w"
        )

        self.status.pack(fill="x", padx=10, pady=(0, 8))

    def build_inputs(self, parent):

        frame = ttk.LabelFrame(parent, text="Input")

        frame.pack(fill="x")

        for row, (key, label) in enumerate(INPUT_FIELDS):
            ttk.Label(frame, text=label, width=15).grid(
                row=row,
                column=0,
                padx=5,
                pady=4,
                sticky="w"
            )

            var = tk.StringVar()

            self.input_vars[key] = var

            ttk.Entry(
                frame,
                textvariable=var,
                width=15
            ).grid(
                row=row,
                column=1,
                padx=5,
                pady=4
            )

    def build_outputs(self, parent):

        frame = ttk.LabelFrame(parent, text="Results")

        frame.pack(fill="both", expand=True)

        for row, (key, label) in enumerate(OUTPUT_FIELDS):
            ttk.Label(frame, text=label, width=18).grid(
                row=row,
                column=0,
                padx=5,
                pady=4,
                sticky="w"
            )

            for solution in range(2):
                var = tk.StringVar()

                self.output_vars[solution][key] = var

                ttk.Entry(
                    frame,
                    textvariable=var,
                    width=14,
                    state="readonly"
                ).grid(
                    row=row,
                    column=solution + 1
                )

    def build_buttons(self):

        frame = ttk.Frame(self.root)

        frame.pack(pady=10)

        ttk.Button(
            frame,
            text="Solve",
            command=self.solve
        ).pack(side="left", padx=5)

        ttk.Button(
            frame,
            text="Clear",
            command=self.clear
        ).pack(side="left", padx=5)

    def solve(self):

        kwargs = {}

        for key, var in self.input_vars.items():
            text = var.get().strip()

            if not text:
                kwargs[key] = 0

                continue

            try:
                kwargs[key] = float(text)

            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    f"'{key}' must be a number."
                )

                return

        try:
            result = solve(**kwargs)

        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex)
            )

            self.status.config(text="Calculation failed.")

            return

        values = ["a", "b", "c", "A", "B", "C", "h_a", "h_b", "h_c", "P", "S", "m_a", "m_b", "m_c", "b_a", "b_b", "b_c", "R", "r"]

        if isinstance(result, tuple):
            solutions = result
            self.status.config(text="Two valid solutions found.")

        else:
            solutions = (result,)
            self.status.config(text="Calculation successful.")

        for i, s in enumerate(solutions):
            for j, key in enumerate(values):
                value = s[j]
                self.output_vars[i][key].set("" if not value else f"{value:.6f}")

        if len(solutions) == 1:
            for var in self.output_vars[1].values():
                var.set("")

    def clear(self):
        for var in self.input_vars.values():
            var.set("")

        for var in self.output_vars[0].values():
            var.set("")

        for var in self.output_vars[1].values():
            var.set("")

        self.status.config(text="Ready.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    TriangleGUI().run()
